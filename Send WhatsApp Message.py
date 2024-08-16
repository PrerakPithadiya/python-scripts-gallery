import pywhatkit
import datetime
from colorama import init, Fore, Style
from art import text2art

init(autoreset=True)


def send_whatsapp_message(recipient_phone_number, message, wait_seconds=10):
    now = datetime.datetime.now()
    _unused_send_time = now + datetime.timedelta(seconds=wait_seconds)

    try:
        pywhatkit.sendwhatmsg_instantly(
            recipient_phone_number, message, wait_time=wait_seconds
        )
        print(
            f"\n{Fore.GREEN}✅ Message sent successfully after {wait_seconds} seconds!{Style.RESET_ALL}"
        )
    except pywhatkit.core.exceptions.CallTimeException as error_msg:
        print(f"\n{Fore.RED}❌ Error: {error_msg}{Style.RESET_ALL}")


def print_fancy_header():
    header = text2art("WhatsApp Sender", font="small")
    print(f"{Fore.CYAN}{header}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{'=' * 50}{Style.RESET_ALL}")


if __name__ == "__main__":
    print_fancy_header()

    phone_number = input(
        f"{Fore.MAGENTA}📞 Enter phone number (+country code): {Style.RESET_ALL}"
    )
    message = input(f"{Fore.GREEN}💬 Enter your message: {Style.RESET_ALL}")

    print(f"\n{Fore.BLUE}🚀 Sending message...{Style.RESET_ALL}")
    send_whatsapp_message(phone_number, message)

    print(
        f"\n{Fore.YELLOW}🎉 Thank you for using WhatsApp Message Sender!{Style.RESET_ALL}"
    )
    print(f"{Fore.CYAN}{'=' * 50}{Style.RESET_ALL}")
