"""
     Собираем подробную информацию о докторах, записываем данные в файл next_data.json и СУБД
"""

import json

import requests
from bs4 import BeautifulSoup

from load_django import *
from parser_app.models import *

# Full headers and cookies
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "referer": "https://www.doctify.com/uk/find/dermatology/london/specialists/page-2",
    "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
}

cookies = {
    "__hstc": "259892885.c6000f6604409abc349dac6e73eeb1de.1732178971391.1732178971391.1732178971391.1",
    "hubspotutk": "c6000f6604409abc349dac6e73eeb1de",
    "__hssrc": "1",
    "_fbp": "fb.1.1732178971891.580218145756924109",
    "euconsent-v2": "CQIcLAAQIcLAAAKA1AENBQFsAP_gAEPgAAwIKlQIAAkACNAMyAgcBB4CHQFMgLTAW2AvMBkgDRwG1gOrAe0BCcCMIElQJOASeAmXBPQE-gJ-QT_BQOCgwKJgUVgouCjMFIAUrgpaCmkFNgU_gqCCokFRgVKBUqA2Ag8BDoCJwF5gMkAe0A_UCSoEywJ6AT7gn6Cf0FBAUIgoWChgFEoKKAotBRkFHIKPAo-BSGCkgKSwUuBS8CmQFNQKeAVAAqMBUoAA.YAAAAAAAAAAA",
    "addtl_consent": "1~89",
    "_ga": "GA1.1.1941564067.1732178972",
    "_gcl_au": "1.1.2037256523.1732178972",
    "_hjSession_1950446": "eyJpZCI6ImQ2MTQ4NzMyLTFiNzctNDg5MS05ZjExLTgyYWU4YzIwMmQzNiIsImMiOjE3MzIxNzg5NzI1MzIsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MX0=",
    "_hjHasCachedUserAttributes": "true",
    "_hjSessionUser_1950446": "eyJpZCI6IjI1M2RkMTY5LWU3YmUtNTk5Yi05NDcxLWJkZDM4NzUyMTljYSIsImNyZWF0ZWQiOjE3MzIxNzg5NzI1MzIsImV4aXN0aW5nIjp0cnVlfQ==",
    "_ga_61XN32XDF0": "GS1.1.1732178970.1.1.1732179162.0.0.0",
    "_ga_2XGSG3QQGT": "GS1.1.1732178970.1.1.1732179162.0.0.0",
    "mp_1060bbf2a606f6a2c4465739e5b5fe55_mixpanel": '{"distinct_id":"$device:1934de98e721245-0b2aeae0d22cda-16462c6e-1fa400-1934de98e721245","$device_id":"1934de98e721245-0b2aeae0d22cda-16462c6e-1fa400-1934de98e721245","$initial_referrer":"$direct","$initial_referring_domain":"$direct","__mps":{},"__mpso":{"$initial_referrer":"$direct","$initial_referring_domain":"$direct"},"__mpus":{},"__mpa":{},"__mpu":{},"__mpr":[],"__mpap":[],"$search_engine":"google"}',
    "__hssc": "259892885.6.1732178971391",
}


for page in range(1, 10000):

    # URL to request
    url = f"https://www.doctify.com/uk/find/dermatology/london/specialists/page-{page}"

    print(f"Getting page {page}")
    # Make the GET request
    response = requests.get(url, headers=headers, cookies=cookies)

    # Search for "__NEXT_DATA__" in the response text
    if "__NEXT_DATA__" in response.text:
        start_index = response.text.find("__NEXT_DATA__")
        data_start = response.text.find("{", start_index)
        data_end = response.text.find("</script>", data_start)
        next_data = response.text[data_start:data_end]

        data = json.loads(next_data)
        # Save to a file
        with open("./../json/next_data.json", "a", encoding="utf-8") as file:
            file.write(next_data + "\n")


        specialists_data = data.get("props", {}).get("pageProps", {}).get("specialists", [])
        soup = BeautifulSoup(response.text, "html.parser")

        if soup.find("nav", class_="MuiPagination-root MuiPagination-text muiltr-1h0c7u0"):

            for specialist in specialists_data:

                doctor_info = {}

                doctor_info["first_name"] = specialist.get("firstName", None).get("en", None)
                doctor_info["last_name"] = specialist.get("lastName", None).get("en", None)
                doctor_info["full_name"] = specialist.get("fullName", None).get("en", None)
                doctor_info["title"] = specialist.get("title", None).get("en", None)
                doctor_info["gender"] = specialist.get("gender", None)
                doctor_info["video_consultation"] = specialist.get("videoConsultation", None)
                doctor_info["practitioner"] = specialist.get("keywords", None)[0].get("practitioner", None).get("en", None)
                doctor_info["description"] = specialist.get("keywords", None)[0].get("description", None).get("en", None)
                doctor_info["keyword_name"]= specialist.get("keywords", None)[0].get("name", None).get("en", None)
                doctor_info["slug"] = specialist.get("keywords", None)[0].get("slug", None)
                doctor_info["about"] = specialist.get("about", None).get("en", None)
                doctor_info["suffix"] = specialist.get("suffix", None).get("en", None) if specialist.get("suffix", None) else None
                doctor_info["explanation"] = specialist.get("explanation", None)
                doctor_info["connections_count"] = specialist.get("connectionsCount", None)
                doctor_info["created_at"] = specialist.get("createdAt", None)
                doctor_info["overall_experience"] = specialist.get("overallExperience", None)
                doctor_info["reviews_total"] = specialist.get("reviewsTotal", None)
                doctor_info["bedside_manner"] = specialist.get("bedsideManner", None)
                doctor_info["average_rating"] = specialist.get("averageRating", None)
                doctor_info["registration_bodies"] = specialist.get("registrationBodies", None)
                doctor_info["last_review"] = specialist.get("lastReview", None)
                doctor_info["post_count"] = specialist.get("postCount", None)
                doctor_info["hide_booking"] = specialist.get("hideBooking", None)
                doctor_info["plan"] = specialist.get("plan", None)
                doctor_info["connections"] = specialist.get("connections", None)
                doctor_info["updated_at"] = specialist.get("updatedAt", None)
                doctor_info["images"] = specialist.get("images", None).get("logo", None)
                doctor_info["statistic"] = specialist.get("statistic", None)
                doctor_info["hide_appointment_request"] = specialist.get("hideAppointmentRequest", None)
                doctor_info["basic"] = specialist.get("basic", None)
                doctor_info["years_as_specialist"] = specialist.get("yearsAsSpecialist", None)
                doctor_info["special_interests"] = specialist.get("specialInterests", None)
                doctor_info["use_single_point_of_contact"] = specialist.get("useSinglePointOfContact", None)
                doctor_info["phone"] = specialist.get("phones", None)
                doctor_info["email"] = specialist.get("emails", None)
                doctor_info["media"] = specialist.get("media", None)
                doctor_info["demo"] = specialist.get("demo", None)
                doctor_info["secretary_name"] = specialist.get("secretaryName", None)
                doctor_info["years_of_experience"] = specialist.get("yearsOfExperience", None)
                doctor_info["medical_procedures"] = specialist.get("medicalProcedures", None)
                doctor_info["languages"]= specialist.get("languages", None)
                doctor_info["external_booking_link"] = specialist.get("externalBookingLink", None)
                doctor_info["logo"] = specialist.get("practices", None)[0].get("images", None).get("logo", None)
                doctor_info["address"] = specialist.get("practices", None)[0].get("address", {})
                doctor_info["working_opening_hours"] = specialist.get("practices", None)[0].get("workingOpeningHours", None)
                doctor_info["public_email_clarification_practice"] = specialist.get("practices", None)[0].get("publicEmailClarificationPractice", None)
                doctor_info["practice_type"] = specialist.get("practices", None)[0].get("type", None)
                doctor_info["contact_details"] = specialist.get("practices", None)[0].get("contactDetails", None)
                doctor_info["public_email_clarification"] = specialist.get("practices", None)[0].get("publicEmailClarification", None)
                doctor_info["reviews"] = specialist.get("practices", None)[0].get("reviews", None)
                doctor_info["external_booking_link_practice"] = specialist.get("practices", None)[0].get("externalBookingLinkPractice", None)
                doctor_info["is_public_system"] = specialist.get("practices", None)[0].get("isPublicSystem", None)
                doctor_info["plan"] = specialist.get("practices", None)[0].get("plan", None)
                doctor_info["consultation_fees"] = specialist.get("consultationFees", None)
                doctor_info["peer_recommendations_count"] = specialist.get("peerRecommendationsCount", None)
                doctor_info["patients_children"] = specialist.get("patientsChildren", None)
                doctor_info["hide_call"] = specialist.get("hideCall", None)
                doctor_info["customer"] = specialist.get("customer", None)
                doctor_info["score"] = specialist.get("score", None)
                doctor_info["statistic_length"] = specialist.get("statisticLength", None)
                doctor_info["education"] = specialist.get("education", {}) if specialist.get("education") else None

                Specialist.objects.update_or_create(
                    full_name=doctor_info["full_name"],
                    defaults=doctor_info
                )
        else:
            break

print("Обновление данных завершено.")

