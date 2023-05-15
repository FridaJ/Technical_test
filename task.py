#! /usr/bin/env python3

# Assummptions about the task:

# Every week gives one sample file
# Each row in samples.txt represents a week (n = 373)

# The second letter of sample name denotes origin; C, T, D, N. In the future there may be more origins

# Write a script that can be run from command line , with output n = how many sequences < 95% covered bases -> qc_pass=False
# It should be divided per origin
# It should send a warning if a certain origin have >10% failed samples
# Implement a system telling the user in some way about the results

#Pseudocode

#read file
#reformat file
#    split on ","
#    TRUE to True
#    FALSE to False
#    find all characters at index 1 in "sample", make list
#        map into new column "origin" for each row
#groupby origin, output qc_pass = False

import sys
import pandas as pd
import numpy as np

#file = sys.argv[1]
file = samples.txt
data = pd.read_csv(file, sep = ',')

data["qc_pass"].replace("TRUE", True)
data["qc_pass"].replace("FALSE", False)

# Make new column with origin from second character in "sample"
origin_list = data["sample"].apply(lambda x = sample[1])
data["origin"] = origin_list
#data["failed"] = data[data["qc_test"] == "FALSE"]]

# I want to make a pivot table here, with the count of "FALSE" in each origin group
groupby_origin = data.groupby("origin")
for origin, qc_pass in groupby_origin['qc_pass']:
    print(origin + "\t" + qc_pass)
    print(data.groupby["origin"].value_counts()["FALSE"])

#p_table = pd.pivot_table(data[data["qc_pass"] == "FALSE"]], index=['origin'])


#Write to file

pd.data_qc.to_csv("result_file_qc")

#Send file as email to recipient if more than 10% failed samples!
# I got this code from Stackoverflow:

import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate


def send_mail(send_from, send_to, subject, text, files=None,
              server="127.0.0.1"):
    assert isinstance(send_to, list)

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    for f in files or []:
        with open(f, "rb") as file:
            part = MIMEApplication(
                file.read(),
                Name=basename(f)
            )
        # After the file is closed
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
        msg.attach(part)


    smtp = smtplib.SMTP(server)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()








