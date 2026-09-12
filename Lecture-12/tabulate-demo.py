import tabulate 
# pip install tabulate 
student =  {
                "id": 1,# should not be updated
                "name":"Karthik",
                "age": 14,
                "dob": "10/01/2012",
                "gender": "male",
                "grade": "grade 7",
                "school": "TridaPro" #should not be updated 
}

tabel = tabulate.tabulate([student],headers="keys",tablefmt="grid")
print(tabel)