import qrcode as qr
image=qr.make("https://www.linkedin.com/in/sabyasachi-sen-4954491b6")
image.save("linkedin_profile.png")