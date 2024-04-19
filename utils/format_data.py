
def format_phone_number(phone: str) -> str:
    return f"+375 ({phone[:2]}) {phone[2:5]}-{phone[5:7]}-{phone[7:9]}"
