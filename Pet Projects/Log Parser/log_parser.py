import re


def main():

    ip_set = {}

    with open('u_ex.log') as f:
        for line in f:
            ip = re.findall("\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}", line)
            # print(ip)
            if ip:
                if ip_set.get(ip[1]):
                    ip_set[ip[1]] += 1
                else:
                    ip_set[ip[1]] = 1

    with open('ip_list.txt', 'a') as f:
        for ip in ip_set:
            f.write(ip + '/n')
    # print(ip_set)


main()
