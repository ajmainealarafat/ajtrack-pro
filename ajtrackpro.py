#!/usr/bin/env python

import os
import time
import requests
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from rich.panel import Panel
from rich.spinner import Spinner
from rich.live import Live

console = Console()

# 📡 IP Info Fetch Function
def fetch_ip_info(ip=""):
    url = f"http://ip-api.com/json/{ip}"
    with Live(Spinner("dots", text="Fetching IP info..."), refresh_per_second=10):
        time.sleep(1)
        r = requests.get(url)
    return r.json()

# 📊 Display Info in Table
def display_info(data):
    if data['status'] != 'success':
        console.print("[bold red]❌ Invalid IP or no data found.[/bold red]")
        return

    table = Table(title="🌐 IP Information", show_lines=True)
    table.add_column("🧾 Field", style="cyan", no_wrap=True)
    table.add_column("📊 Value", style="magenta")

    fields = {
        "IP Address": data.get('query', '-'),
        "City": data.get('city', '-'),
        "Region": data.get('regionName', '-'),
        "Country": data.get('country', '-'),
        "Timezone": data.get('timezone', '-'),
        "ISP": data.get('isp', '-'),
        "Organization": data.get('org', '-'),
        "Lat, Long": f"{data.get('lat', '-')}, {data.get('lon', '-')}"
    }

    for field, value in fields.items():
        table.add_row(field, value)

    console.print(table)

# 🚀 Main Menu
def main():
    os.system("clear")  # পুরাতন আউটপুট মুছে দাও

    console.print(Panel.fit(
        "[bold green]🚀 Welcome to AjTrack Pro[/bold green]\n"
        "[dim]Stylish IP Tracker with Python & Rich[/dim]",
        title="🔥 AjTrack Pro", subtitle="Created by Ajmaine Al Arafat"))

    while True:
        console.print(Panel.fit(
            "[bold yellow]🎯 AjTrack Pro - by Ajmaine Al Arafat[/bold yellow]\n\n"
            "[green]1[/green]: 🌐 Track Custom IP\n"
            "[green]2[/green]: 🧑‍💻 Show Your Own IP Info\n"
            "[green]3[/green]: ❌ Exit",
            title="💻 Main Menu", subtitle="Choose wisely! 🚀"))

        choice = Prompt.ask("🤔 Select an option", choices=["1", "2", "3"], default="3")

        if choice == "1":
            ip = Prompt.ask("🔍 Enter IP address")
            data = fetch_ip_info(ip)
            display_info(data)
        elif choice == "2":
            data = fetch_ip_info()
            display_info(data)
        else:
            console.print("[bold green]👋 Thanks for using AjTrack Pro! Goodbye![/bold green]")
            break

        Prompt.ask("\n👉 Press ENTER to return to menu...")

    # 📌 Developer Credits
    console.print(Panel.fit(
        "[bold cyan]🔧 Made with ❤️ by [bold yellow]Ajmaine Al Arafat[/bold yellow][/bold cyan]\n"
        "[link=https://github.com/ajmainealarafat]🌐 GitHub: ajmainealarafat[/link]",
        title="📌 Credits", subtitle="Support the Creator 🚀"))

# ▶️ Run
if __name__ == "__main__":
    main()
