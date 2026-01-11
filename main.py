import json

OUTPUT_FILE = "bangladesh_holidays_2026.json"

t = '{"holidays": [{"startDate": "2026-02-04", "endDate": "2026-02-04", "holiday_name": "শব-এ-বারাত", "type": "Religious"}, {"startDate": "2026-02-21", "endDate": "2026-02-21", "holiday_name": "শহীদ দিবস", "type": "National"}, {"startDate": "2026-03-17", "endDate": "2026-03-17", "holiday_name": "শেখ মুজিবুর রহমানের জন্মদিন", "type": "National"}, {"startDate": "2026-03-18", "endDate": "2026-03-18", "holiday_name": "লাইলাতুল কদর", "type": "Religious"}, {"startDate": "2026-03-19", "endDate": "2026-03-23", "holiday_name": "ঈদুল ফিতর", "type": "Religious"}, {"startDate": "2026-03-20", "endDate": "2026-03-20", "holiday_name": "জুমাতুল বিদা", "type": "Religious"}, {"startDate": "2026-03-26", "endDate": "2026-03-26", "holiday_name": "স্বাধীনতা দিবস", "type": "National"}, {"startDate": "2026-04-14", "endDate": "2026-04-14", "holiday_name": "পহেলা বৈশাখ", "type": "National"}, {"startDate": "2026-05-01", "endDate": "2026-05-01", "holiday_name": "মে দিবস", "type": "National"}, {"startDate": "2026-05-22", "endDate": "2026-05-22", "holiday_name": "বুদ্ধ পূর্ণিমা", "type": "Religious"}, {"startDate": "2026-05-26", "endDate": "2026-05-30", "holiday_name": "ঈদুল আযহা", "type": "Religious"}, {"startDate": "2026-06-26", "endDate": "2026-06-26", "holiday_name": "আশুরা", "type": "Religious"}, {"startDate": "2026-08-15", "endDate": "2026-08-15", "holiday_name": "জাতীয় শোক দিবস", "type": "National"}, {"startDate": "2026-08-25", "endDate": "2026-08-25", "holiday_name": "ঈদে মিলাদুন নবী", "type": "Religious"}, {"startDate": "2026-09-04", "endDate": "2026-09-04", "holiday_name": "শ্রী কৃষ্ণ জন্মাষ্টমী", "type": "Religious"}, {"startDate": "2026-10-21", "endDate": "2026-10-21", "holiday_name": "বিজয়াদশমী", "type": "Religious"}, {"startDate": "2026-12-16", "endDate": "2026-12-16", "holiday_name": "বিজয় দিবস", "type": "National"}, {"startDate": "2026-12-25", "endDate": "2026-12-25", "holiday_name": "ক্রিসমাস", "type": "Religious"}]}'

def main():
    data = json.loads(t or '{}')
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"🎉 Success! Holidays saved to '{OUTPUT_FILE}'")
    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()
