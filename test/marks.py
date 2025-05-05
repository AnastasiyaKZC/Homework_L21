
import allure


# def microservice(name):
#     return allure.label("msrv", name)
#
#
# def owner(name):
#     return allure.label("owner", name)
#
#
# def layer(name):
#     return allure.label("layer", name)
#
#
# def tm4j(issue):
#     return allure.label("tm4j", issue)
#
#
# def jira_issues(*issues):
#     return allure.label("jira", *issues)

def microservice(name):
    return allure.label("tag", f"msrv:{name}")

def owner(name):
    return allure.label("owner", name)  # исправлено

def layer(name):
    return allure.label("tag", f"layer:{name}")

def tm4j(issue):
    return allure.label("tag", f"tm4j:{issue}")

def jira_issues(*issues):
    return allure.label("issue", *issues)  # использует встроенную метку
