prompt = """
You are a data extraction assistant.
Below is raw search data about Public Holidays in Bangladesh for the year 2026.

Task:
1. Extract all holidays mentioned in the search Data.
2. Format the output as a strict JSON list of objects.
3. Each object must have: "startDate" and "endDate" (YYYY-MM-DD or string if variable), "holiday_name", and "type" (if available, e.g., National, Religious).
4. If exact dates differ between sources (due to moon sightings for Eid), use the most likely date mentioned. must use date range for multi-day holidays.
5. Do NOT include markdown formatting (like ```json). Just the raw JSON string.
6. Return a JSON object with three keys:
    - "startDate": string<YYYY-MM-DD>
    - "endDate": string<YYYY-MM-DD>
    - "holiday_name": string<Converted into Bangla>
    - "type": National | Religious

Output example:
'{"holidays": [{"startDate": "YYYY-03-02", "endDate": "YYYY-03-06", "holiday_name_bn": "ঈদুল আজহা", "holiday_name_en": "Eid ul Azha", "type": "Religious"}, ... ]}'


Search Data:
"""