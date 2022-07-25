import random

trainees = []
clients = []
centres = []
courses_list = ["Java", "C#", "Data", "DevOps", "Business"]
close_TH = 0


# condition = "training", "waiting list", "client", "bench"
class Trainee:
    def __init__(self, course, condition):
        self.course = course
        self.condition = condition
        # every month this value will increase when the trainee is in condition == "training"
        self.month = 0


# condition = open, full, closed
class Centre:
    def __init__(self):
        pass

    def distribute_trainees(self):
        # 9) check if the centre is still open before assigning trainees
        if centre.condition == "open":
            rand = random.randint(0, 50)
            # check for number of vacancies in the center
            vacancies = centre.capacity - centre.trainees
            if vacancies < rand:
                # the center will only take the number of trainees = to the vacancies
                rand = vacancies

            while rand >= 0:
                # assign trainees to learning centres
                for trainee in trainees:
                    if trainee.condition == "waiting list":
                        if centre.kind == "Tech Centre" and centre.course.key() == trainee.course:
                            trainee.condition = "training"
                            centre.course[trainee.course].append(trainee)
                            centre.trainees += 1
                        elif centre.kind == "Bootcamp" or centre.kind == "Training Hub":
                            trainee.condition = "training"
                            centre.course[trainee.course].append(trainee)
                            centre.trainees += 1
                        else:
                            continue
                        # 10) check if the centre is full after assigning trainees
                        if centre.trainees == centre.capacity:
                            centre.condition = "full"
                        rand -= 1
                        if rand == 0:
                            break
                break

    def check_trainees(self):
        # 12) close bootcamps with less than 25 trainees for 3 months
        if centre.kind == "Bootcamp" and centre.trainees < 25:
            centre.close_BC += 1
            if centre.close_BC == 4:
                centre.condition = "closed"
                # 14) move trainees to other centres
                centre.move_trainees()
        if centre.kind == "Bootcamp" and centre.trainees >= 25:
            centre.close_BC = 0
        # 13) close centres with less than 25 trainees
        if (centre.kind == "Training Hub" or centre.kind == "Tech Centre") and centre.trainees < 25:
                centre.condition = "closed"
                # move trainees to waiting list
                centre.move_trainees()

    def move_trainees(self):
        # 14) move trainees to waiting list
        # iterate over the dictionary; list_trainees is a list containing the trainees studying in each course
        for list_trainees in centre.course.values():
            # iterate over the items in the list containing the trainees studying in each course
            # t is each of the trainees
            for trainee in list_trainees:
                trainee.condition = "waiting list"
                # remove the trainee from the list list_trainees
                list_trainees.remove(trainee)


# can train a maximum of 100 trainees but 3 can be opened at a time each month
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
        self.course = {course_key: []}
        self.kind = "Tech Centre"
        self.capacity = 200
        self.trainees = len(self.course[course_key])


class Clients:
    def __init__(self, trainee_req, month, course_key):
        self.trainee_req = trainee_req
        self.trainees = []
        self.month = month
        self.course = {course_key:""}

    def assign_trainees(self):
        # check if the client needs trainees
        if len(client.trainees) < client.trainee_req:
            # calculate the number of trainees needed
            trainees_needed = client.trainee_req - len(client.trainees)
            # assign trainees to existing clients
            while trainees_needed > 0:
                for trainee in trainees:
                    if trainee.condition == "bench" and trainee.course == client.course:
                        trainee.condition = "client"
                        client.trainees.append(trainee)
                        trainees_needed -= 1
                break

    def unsatisfied_client(self):
        if len(client.trainees) < client.trainee_req:
            # move trainees to bench and delete client
            for trainee in client.trainees:
                trainee.condition = "bench"
                clients.remove(client)
        # reset the original value of trainees required for satisfied clients
        else:
            client.trainee_req *= num/12

user_months = int(input(" Enter the number of months for the simulation:\n"))
user_option = int(input(" For monthly results enter: 1\n For results at the end enter: 2 \n"))

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
        clients.append(Clients(trainees_req, num, course))

    # EVERY 2 MONTHS
    if num % 2 == 0:
        # 15) open 1 centre
        # check if less than 2 bootcamps are open
        center_type = random.choice(["Training Hub", "Bootcamp", "Tech Centre"])
        if center_type == "Bootcamp":
            # check the number of Bootcamps opened, and if less than 2 open one
            count = 0
            for i in range(0,len(centres)-1):
                if centres[i].kind == "Bootcamp" and centres[i].condition == "open":
                    count += 1
            if count < 2:
                centres.append(Bootcamp("open", num))
            # else choose between Training Hub or Tech Centre
            else:
                center_type = random.choice(["Training Hub", "Tech Centre"])
                if center_type == "Training Hub":
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

        elif center_type == "Training Hub":
            count = 0
            for i in range(0,len(centres)-1):
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

    # 6) create 50 to 100 new trainees
    num_trainees = random.randrange(50, 101)
    while num_trainees > 0:
        # 7) random assignment of trainee to courses
        option = random.choice(courses_list)
        # create a new trainee and append it to the trainees list
        trainees.append(Trainee(option, "waiting_list"))
        num_trainees -= 1

    # 8) each center takes 0 to 50 trainees
    for centre in centres:
        # trainees taken by centres
        centre.distribute_trainees()
        # 11) check for number of trainees for centre
        # 12) close bootcamps with less than 25 trainees for 3 months
        # 13) close centres with less than 25 trainees
        centre.check_trainees()
        # 14) move trainees to another centre
        centre.move_trainees()

    if user_option == 1:
        # show the number of open centres
        open_centres = 0
        full_centres = 0
        closed_centres = 0

        for centre in centres:
            if centre.condition == "open":
                open_centres += 1
            if centre.condition == "full":
                full_centres += 1
            if centre.condition == "closed":
                closed_centres += 1

        # show the number of trainees currently training
        trainees_training = 0
        trainees_waiting = 0
        trainees_bench = 0

        for trainee in trainees:
            if trainee.condition == "training":
                trainees_training += 1
            if trainee.condition == "waiting list":
                trainees_waiting += 1
            if trainee.condition == "bench":
                trainees_bench += 1

        print(f"Open centres: {open_centres}")
        print(f"Full centres: {full_centres}")
        print(f"Closed centres: {closed_centres}")
        print(f"Trainees on training condition: {trainees_training}")
        print(f"Trainees on waiting list condition: {trainees_waiting}")
        print(f"Trainees on bench condition: {trainees_bench}")

    num += 1

if user_option == 2:
    # show the number of open centres
    open_centres = 0
    full_centres = 0
    closed_centres = 0

    for centre in centres:
        if centre.condition == "open":
            open_centres += 1
        if centre.condition == "full":
            full_centres += 1
        if centre.condition == "closed":
            closed_centres += 1

    # show the number of trainees currently training
    trainees_training = 0
    trainees_waiting = 0
    trainees_bench = 0

    for trainee in trainees:
        if trainee.condition == "training":
            trainees_training += 1
        if trainee.condition == "waiting list":
            trainees_waiting += 1
        if trainee.condition == "bench":
            trainees_bench += 1

    print(f"Open centres: {open_centres}")
    print(f"Full centres: {full_centres}")
    print(f"Closed centres: {closed_centres}")
    print(f"Trainees on training condition: {trainees_training}")
    print(f"Trainees on waiting list condition: {trainees_waiting}")
    print(f"Trainees on bench condition: {trainees_bench}")
