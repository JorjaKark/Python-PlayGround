def fight(heroes, villain):
    for i in heroes:
        if i["category"] == villain["category"]:
            if i["health"] >= villain["health"]:
                return (i["name"]+ " defeated the villain and now has a score of "+ str(i["score"] + 1))
            else:
                villain["health"] -= i["health"] / 2
    return (villain["name"]+ " prevailed with "+ str(round(villain["health"], 1))+ "HP left")
