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
        # 9) check if the centre is still open before assigning trainees
        if centre.condition == "open":
            # assign a random number of trainees to the centre
            rand = random.randint(0, 50)
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

    def check_trainees(self):
        # 12) close bootcamps with less than 25 trainees for 3 months
        if centre.kind == "Bootcamp" and centre.trainees < 25:
            centre.close_BC += 1
            if centre.close_BC == 4:
                centre.condition = "closed"
                # move trainees to waiting list
                for list_trainees in centre.course.values():
                    # iterate over the items in the list containing the trainees studying in each course
                    # t is each of the trainees
                    for trainee in list_trainees:
                        trainee.condition = "waiting list"
                        # remove the trainee from the list list_trainees
                    list_trainees.clear()
        if centre.kind == "Bootcamp" and centre.trainees >= 25:
            centre.close_BC = 0
        # 13) close centres with less than 25 trainees
        if (centre.kind == "Training Hub" or centre.kind == "Tech Centre") and centre.trainees < 25:
            centre.condition = "closed"
            centre.trainees = 0
            # move trainees to waiting list
            for list_trainees in centre.course.values():
                # iterate over the items in the list containing the trainees studying in each course
                for tr_item in list_trainees:
                    tr_item.condition = "waiting list"
                # remove the trainees from the list list_trainees
                list_trainees.clear()


class TrainingHub(Centre):
    def __init__(self, condition, month):
        self.course = {"Java": [], "C#": [], "Data": [], "DevOps": [], "Business": []}
        self.condition = condition
        self.month = month
        self.kind = "Training Hub"
        self.capacity = 100
        self.trainees = 0
        self.close_TH = 0


# can train a maximum of 500 trainees
class Bootcamp(Centre):
    def __init__(self, condition, month):
        self.course = {"Java": [], "C#": [], "Data": [], "DevOps": [], "Business": []}
        self.condition = condition
        self.month = month
        self.kind = "Bootcamp"
        self.capacity = 500
        self.trainees = 0
        self.close_BC = 0


# Can train 200 trainees but only teaches one course per centre
# when I open this kind of centre I will randomly assign a kind of course
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
                    client.trainees.append(trainee)
                    trainees_needed -= 1
                if trainees_needed == 0:
                    break

    def unsatisfied_client(self):
        if len(client.trainees) < client.trainee_new_req:
            print("delete client")
            # move trainees to bench and delete client
            for trainee in client.trainees:
                trainee.condition = "bench"
            clients.remove(client)
        # reset the original value of trainees required for satisfied clients
        else:
            client.trainee_new_req += client.trainee_req

user_months = 200
num = 1

while num <= user_months:

    # EVERY 12 MONTHS
    if num % 12 == 0:
        # 5) delete unsatisfied clients (didn't fulfill requirement within a year)
        for client in clients:
            client.unsatisfied_client()
        # Create a new client
        # Generate the trainees requirement between 15 and 30 (randrange is not inclusive)
        trainees_req = random.randrange(15, 31)
        course = random.choice(courses_list)
        clients.append(Client(trainees_req, num, course))

    # EVERY 2 MONTHS
    if num % 2 == 0:
        # 15) open 1 centre
        # check the number of Bootcamps: only 2 can ever exist
        if count_BC < 2:
            center_type = random.choice(["Training Hub", "Bootcamp", "Tech Centre"])
            if center_type == "Bootcamp":
                centres.append(Bootcamp("open", num))
                count_BC += 1
            elif center_type == "Training Hub":
                # check the number of Training Hubs opened, and if less than 3 open one
                count = 0
                for i in range(0, len(centres) - 1):
                    if centres[i].kind == "Training Hub" and centres[i].condition == "open":
                        count += 1
                if count < 3:
                    centres.append(TrainingHub("open", num))
                else:
                    # open a Tech Centre and assign a random course to the centre
                    course = random.choice(courses_list)
                    centres.append(TechCentre("open", num, course))
            else:
                # open a Tech Centre and assign a random course to the centre
                course = random.choice(courses_list)
                centres.append(TechCentre("open", num, course))

        else:
            # choose between Training Hub or Tech Centre
            center_type = random.choice(["Training Hub", "Tech Centre"])
            if center_type == "Training Hub":
                count = 0
                for i in range(0, len(centres) - 1):
                    if centres[i].kind == "Training Hub" and centres[i].condition == "open":
                        count += 1
                if count < 3:
                    centres.append(TrainingHub("open", num))
                else:
                    # open a Tech Centre and assign a random course to the centre
                    course = random.choice(courses_list)
                    centres.append(TechCentre("open", num, course))
            else:
                # open a Tech Centre and assign a random course to the centre
                course = random.choice(courses_list)
                centres.append(TechCentre("open", num, course))

    # EVERY MONTH
    # 1) increase the month value for the trainees doing training
    for trainee in trainees:
        if trainee.condition == "training":
            trainee.month += 1
        # 2) after 12 months of training move trainees to bench
        if trainee.month == 12:
            trainee.condition = "bench"

    # 3) assign trainees to existing clients
    for client in clients:
        # check if the client needs trainees
        client.assign_trainees()
        for trainee in client.trainees:
            trainee.condition = "client"

    # 6) create 50 to 100 new trainees
    num_trainees = random.randrange(50, 101)
    while num_trainees > 0:
        # 7) random assignment of trainee to courses
        option = random.choice(courses_list)
        # create a new trainee and append it to the trainees list
        trainees.append(Trainee(option, "waiting list"))
        num_trainees -= 1

    for centre in centres:
        # the trainees are distributed to the centres
        centre.distribute_trainees()
        # 11) check for number of trainees for centre
        # 12) close bootcamps with less than 25 trainees for 3 months
        # 13) close centres with less than 25 trainees
        centre.check_trainees()

    num += 1

results = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for centre in centres:
    if centre.condition == "open":
        results[0] += 1
        if centre.kind == "Bootcamp":
            results[1] += 1
        elif centre.kind == "Training Hub":
            results[2] += 1
        elif centre.kind == "Tech Centre":
            results[3] += 1

    if centre.condition == "full":
        results[4] += 1
        if centre.kind == "Bootcamp":
            results[5] += 1
        elif centre.kind == "Training Hub":
            results[6] += 1
        elif centre.kind == "Tech Centre":
            results[7] += 1

    if centre.condition == "closed":
        results[8] += 1
        if centre.kind == "Bootcamp":
            results[9] += 1
        elif centre.kind == "Training Hub":
            results[10] += 1
        elif centre.kind == "Tech Centre":
            results[11] += 1

for trainee in trainees:
    if trainee.condition == "training":
        results[12] += 1
        if trainee.course == "Java":
            results[13] += 1
        elif trainee.course == "C#":
            results[14] += 1
        elif trainee.course == "Data":
            results[15] += 1
        elif trainee.course == "DevOps":
            results[16] += 1
        elif trainee.course == "Business":
            results[17] += 1
    elif trainee.condition == "waiting list":
        results[18] += 1
        if trainee.course == "Java":
            results[19] += 1
        elif trainee.course == "C#":
            results[20] += 1
        elif trainee.course == "Data":
            results[21] += 1
        elif trainee.course == "DevOps":
            results[22] += 1
        elif trainee.course == "Business":
            results[23] += 1
    elif trainee.condition == "bench":
        results[24] += 1
        if trainee.course == "Java":
            results[25] += 1
        elif trainee.course == "C#":
            results[26] += 1
        elif trainee.course == "Data":
            results[27] += 1
        elif trainee.course == "DevOps":
            results[28] += 1
        elif trainee.course == "Business":
            results[29] += 1
    elif trainee.condition == "client":
        results[30] += 1

results[31] = len(centres)
print(f"\nTotal centres: {results[31]}")
print(f"\nOpen centres: {results[0]}")
print(f"   Bootcamps: {results[1]}")
print(f"   Training Hubs: {results[2]}")
print(f"   Tech Centres: {results[3]}")
print(f"Full centres: {results[4]}")
print(f"   Bootcamps: {results[5]}")
print(f"   Training Hubs: {results[6]}")
print(f"   Tech Centres: {results[7]}")
print(f"Closed centres: {results[8]}")
print(f"   Bootcamps: {results[9]}")
print(f"   Training Hubs: {results[10]}")
print(f"   Tech Centres: {results[11]}")

results[32] = len(trainees)
print(f"\nTotal trainees: {results[32]}")
print(f"\nTrainees currently training: {results[12]}")
for item in courses_list:
    print(f"   {item}: {results[courses_list.index(item) + 13]}")
print(f"Trainees on the waiting list: {results[18]}")
for item in courses_list:
    print(f"   {item}: {results[courses_list.index(item) + 19]}")
print(f"Trainees on the bench: {results[24]}")
for item in courses_list:
    print(f"   {item}: {results[courses_list.index(item) + 25]}")
print(f"Trainees with a client: {results[30]}")
print(" ------------------------------------------------")

# for centre in centres:
#     print(
#         f"\nCentre number {centres.index(centre) + 1}: {centre.kind} - Trainees: {centre.trainees} - {centre.condition} - {centre.month}")
#     for course, trainees in centre.course.items():
#         print(f"   Course: {course} - Trainees: {len(trainees)}")
#         for trainee in trainees:
#             if centre.condition == "closed":
#                 print(trainee.condition)

results[33] = len(clients)
print(f"\nTotal clients: {results[33]}")
for client in clients:
    print(f"Client month: {client.month} - Trainees requirement: {client.trainee_new_req} - Trainees: {len(client.trainees)}")

