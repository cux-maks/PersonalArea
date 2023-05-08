money = {
    "quarter":25,
    "dime":10,
    "nickel":5,
    "penny":1
}


T = int(input())
for _ in range(T):
    val = int(input())
    print(val//money["quarter"], end = " ")
    val %= money["quarter"]
    print(val//money["dime"], end = " ")
    val %= money["dime"]
    print(val//money["nickel"], end = " ")
    val %= money["nickel"]
    print(val//money["penny"])
    