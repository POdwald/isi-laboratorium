import csv

def generate_pc_csv(file_path):
    with open(file_path, 'w', newline='') as csvfile:
        fieldnames = ['pc_name', 'ip']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for i in range(1, 101):
            pc_name = f'P{i:03}'
            ip_address = f'172.30.2.{i}'
            writer.writerow({'pc_name': pc_name, 'ip': ip_address})

if __name__ == '__main__':
    file_path = 'pc.csv'
    generate_pc_csv(file_path)
    print(f"Plik 'pc.csv' został pomyślnie utworzony.")