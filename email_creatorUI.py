import customtkinter as ctk
from customtkinter import filedialog
from email_functions import generate_email, change_tone

  
ctk.set_appearance_mode("Dark")

root = ctk.CTk()
root.geometry("1000x1000")

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill="both", expand=True)

title = ctk.CTkLabel(master=frame, text="Email Creator Tool", font=("Outfit", 24))
title.pack(pady=12, padx=10)

entry_frame = ctk.CTkFrame(master=frame)
entry_frame.pack(padx=10, pady=18)

# Place the "Video URL" entry field and "Only Audio" checkbox in the same line
email_prompt = ctk.CTkEntry(master=entry_frame, placeholder_text="Email prompt", width=250)
email_prompt.pack(side="left", padx=13)

email_body_frame = ctk.CTkFrame(master=frame)
email_body_frame.pack(padx=10,pady=30)


email_body = ctk.CTkTextbox(master=email_body_frame, height=400, width=700, font=("Outfit", 18))
email_body.pack()

generate_button = ctk.CTkButton(master=entry_frame, text="Generate Email",
                        width=130, fg_color = "#06a5c4",
                        hover_color="#046b80", font=ctk.CTkFont(family='Outfit', size=14),
                         command=lambda: generate_email(prompt=email_prompt.get(), body=email_body))
generate_button.pack(side="left",pady=20, padx=10)


tone_frame = ctk.CTkFrame(master=frame)
tone_frame.pack(ipadx = 40, ipady = 10, pady=20)

label = ctk.CTkLabel(master=tone_frame, text="Make it more:",font=("Outfit",22))
label.pack(side="top",pady = 7, padx = 2)
formal_button = ctk.CTkButton(master=tone_frame, text="Formal",
                        width=150,
                        height=40, fg_color="#828181", hover_color="#525252",
                        font=ctk.CTkFont(family='Outfit', size=16),
                        command=lambda: change_tone(tone="formal", body=email_body),
                        corner_radius=20
                        )

casual_button = ctk.CTkButton(master=tone_frame, text="Casual",
                        width=150,
                        height=40, fg_color="#009933", hover_color="#006622",
                        font=ctk.CTkFont(family='Outfit', size=16),
                        command=lambda: change_tone(tone="casual", body=email_body),
                        corner_radius=20
                        )
friendly_button = ctk.CTkButton(master=tone_frame, text="Friendly",
                        width=150,
                        height=40, fg_color="#fc7005", hover_color="#a65305",
                        font=ctk.CTkFont(family='Outfit', size=16),
                        command=lambda: change_tone(tone="friendly", body=email_body),
                        corner_radius=20,
                        )

vulgar_button = ctk.CTkButton(master=tone_frame, text="Vulgar",
                        width=150,
                        height=40, fg_color="red", hover_color="#a65305",
                        font=ctk.CTkFont(family='Outfit', size=16),
                        command=lambda: change_tone(tone="vulgar", body=email_body),
                        corner_radius=20,
                        )
disrespectful_button = ctk.CTkButton(master=tone_frame, text="Disrespectful",
                        width=150,
                        height=40, fg_color="red", hover_color="#a65305",
                        font=ctk.CTkFont(family='Outfit', size=16),
                        command=lambda: change_tone(tone="disrespectful", body=email_body),
                        corner_radius=20,
                        )
formal_button.pack(side="left",pady = 13, padx = 10)
casual_button.pack(side="left",pady = 13, padx = 10)
friendly_button.pack(side="left",pady = 13, padx = 10)
vulgar_button.pack(side="left",pady = 13, padx = 10)
disrespectful_button.pack(side="left",pady = 13, padx = 10)
root.mainloop()