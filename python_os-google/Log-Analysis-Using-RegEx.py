import csv
import operator
import re

"""Code for errors count"""
err_dict = {}

with open('syslog.log') as f:
    for line in f:
        res_err = re.search(r"ticky: ERROR ([\w ']*) ", line)
        if res_err:
            key = res_err[1].strip()
            err_dict[key] = err_dict.get(key, 0) + 1

err_list_sorted = sorted(err_dict.items(), key=operator.itemgetter(1), reverse=True)
err_list_sorted.insert(0, ('Error', 'Count'))

with open('error_messages.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for t in err_list_sorted:
        writer.writerow(t)


"""Code for user stats"""
username_info_dict = {}
username_error_dict = {}
with open('syslog.log') as f:
    for line in f:
        res_info = re.search(r"ticky: INFO.*\((.*)\)", line)
        res_err = re.search(r"ticky: ERROR.*\((.*)\)", line)
        if res_err:
            key = res_err[1]
            username_error_dict[key] = username_error_dict.get(key, 0) + 1
        if res_info:
            key = res_info[1]
            username_info_dict[key] = username_info_dict.get(key, 0) + 1

username_all_dict = {}
for user in username_info_dict.keys():
    username_all_dict[user] = [username_info_dict.get(user)]
    username_all_dict[user].append(username_error_dict.pop(user, 0))

for user in username_error_dict.keys():
    username_all_dict[user] = [0, username_error_dict.get(user)]

username_list_sorted = sorted(username_all_dict.items())

with open('user_statistics.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(("Username", "INFO", "ERROR"))
    for t in username_list_sorted:
        # writer.writerow((t[0], t[1][0], t[1][1]))
        writer.writerow((t[0], *t[1]))
