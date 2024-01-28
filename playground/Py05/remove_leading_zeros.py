def remove_leading(ip):

    parts = ip.split(".")


    parts = [str(int(part)) if part != '0' else '0' for part in parts]

    result_ip = ".".join(parts)

    return result_ip
