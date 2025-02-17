import csv


class form:
    def __init__(self):
        pass

    def write_to_file(self, data):
        with open('database.txt', mode='a') as database:
            email = data["email"]
            subject = data["subject"]
            message = data["message"]
            file = database.write(f'\n{email},{subject},{message}')

    def write_to_csv(self, data):
        with open('database.csv', mode='a', newline='') as database2:
            email = data["email"]
            subject = data["subject"]
            message = data["message"]
            csv_writer = csv.writer(database2, delimiter=',',
                                    quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([email, subject, message])
