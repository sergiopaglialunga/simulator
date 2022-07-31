import random

trainees = []
centres = []
clients = []
courses_list = ["Java", "C#", "Data", "DevOps", "Business"]
count_TH = 0
count_BC = 0


class Trainee:
    def __init__(self, course, condition):
        self.course = course
        self.condition = condition
        # every month this value will increase when the trainee is in condition == "training"
        self.month = 0


class Centre:
    def __init__(self):
        pass

    def distribute_trainees(self):
        # 9) check if the centre is open before assigning trainees
        if centre.condition == "open":
            # assign a random number of trainees to the centre
            rand = 20
            # check for number of vacancies in the center
            vacancies = centre.capacity - centre.trainees
            if vacancies < rand:
                # the center will only take the number of trainees = to the vacancies
                rand = vacancies

            while rand > 0:
                # assign trainees to learning centres
                for trainee in trainees:
                    if trainee.condition == "waiting list":
                        if centre.kind == "Tech Centre":
                            if centre.course_name == trainee.course:
                                trainee.condition = "training"
                                centre.course[trainee.course].append(trainee)
                                centre.trainees += 1
                                rand -= 1
                            else:
                                continue
                        elif centre.kind == "Bootcamp" or centre.kind == "Training Hub":
                            trainee.condition = "training"
                            centre.course[trainee.course].append(trainee)
                            centre.trainees += 1
                            rand -= 1
                        # 10) check if the centre is full after assigning trainees
                        if centre.trainees == centre.capacity:
                            centre.condition = "full"
                        # check if all the trainees were distributed
                        if rand == 0:
                            break
                break


class TechCentre(Centre):
    def __init__(self, condition, month, course_key):
        self.condition = condition
        self.month = month
        self.course = {course_key:[]}
        self.kind = "Tech Centre"
        self.course_name = course_key
        self.capacity = 200
        self.trainees = 0


class Client:
    def __init__(self, trainee_req, month, course):
        self.trainee_req = trainee_req
        self.trainee_new_req = trainee_req
        self.month = month
        self.course = course
        self.trainees = []

    def assign_trainees(self):
        # check if the client needs trainees
        if len(client.trainees) < client.trainee_new_req:
            # calculate the number of trainees needed
            trainees_needed = client.trainee_new_req - len(client.trainees)
            # assign trainees to existing clients
            for trainee in trainees:
                if trainee.condition == "bench" and client.course == trainee.course:
                    trainee.condition = "client"
                    client.trainees.append(trainee)
                    trainees_needed -= 1
                if trainees_needed == 0:
                    break
            for trainee in client.trainees:
                trainee.condition = "client"

    def unsatisfied_client(self):
        print(client.month, len(client.trainees), client.trainee_new_req)
        if len(client.trainees) < client.trainee_new_req:
            #
            # move trainees to bench and delete client
            for trainee in client.trainees:
                print(trainee.condition)
                trainee.condition = "bench"
                print(trainee.condition)
            clients.remove(client)
        # reset the original value of trainees required for satisfied clients
        else:
            client.trainee_new_req = int(trainees_req * (num/client.month))


user_months = 26
num = 1

while num <= user_months:
    # EVERY 12 MONTHS: create a client
    # Delete unsatisfied clients (didn't fulfill requirement within a year)
    # and restart the trainee requirement for satisfied clients
    # for client in clients:
    #     client.unsatisfied_client() # CLIENT 1

    if num % 12 == 0:
        course = random.choice(courses_list)
        clients.append(Client(10, num, course))

    # EVERY 2 MONTHS: create a centre
    if num % 2 == 0:
        course = random.choice(courses_list)
        centres.append(TechCentre("open", num, course))

    # EVERY MONTH: create trainees
    # 1) increase the month value for the trainees doing training
    for trainee in trainees:
        if trainee.condition == "training":
            trainee.month += 1
        # 2) after 12 months of training move trainees to bench
        if trainee.month == 12:
            trainee.condition = "bench"

    # 3) assign trainees to existing clients
    for client in clients:
    #     # check if the client needs trainees
        client.assign_trainees() # CLIENT 2
        for trainee in client.trainees:
            trainee.condition = "client"
    # 6) create 50 to 100 new trainees
    num_trainees = 10
    while num_trainees > 0:
        # 7) random assignment of trainee to courses
        option = random.choice(courses_list)
        # create a new trainee and append it to the trainees list
        trainees.append(Trainee(option, "waiting list"))
        num_trainees -= 1

    for centre in centres:
        # the trainees are distributed to the centres
        centre.distribute_trainees() # CENTRE 1
        # 11) check for number of trainees for centre
        # 12) close bootcamps with less than 25 trainees for 3 months
        # 13) close centres with less than 25 trainees
        # centre.check_trainees() # CENTRE 2

    num += 1


results = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for centre in centres:
    if centre.condition == "open":
        results[0] += 1
    if centre.condition == "full":
        results[4] += 1
    if centre.condition == "closed":
        results[8] += 1

for trainee in trainees:
    if trainee.condition == "training":
        results[12] += 1
    elif trainee.condition == "waiting list":
        results[18] += 1
    elif trainee.condition == "bench":
        results[24] += 1
    elif trainee.condition == "client":
        results[30] += 1

print(f"\nTotal centres: {len(centres)}")
print(f"\nOpen centres: {results[0]}")
print(f"Full centres: {results[4]}")
print(f"Closed centres: {results[8]}")

print(f"\nTrainees: {len(trainees)}")
print(f"\nTrainees currently training: {results[12]}")
print(f"Trainees on the waiting list: {results[18]}")
print(f"Trainees on the bench: {results[24]}")
print(f"Trainees with a client: {results[30]}")
print(" ------------------------------------------------")

results[32] = len(clients)
print(f"Total clients: {results[32]}")
for client in clients:
    print(f"Client month: {client.month} - Trainees requirements: {client.trainee_req} - Trainees: {len(client.trainees)}")
    for trainee in client.trainees:
        print(trainee.condition)

