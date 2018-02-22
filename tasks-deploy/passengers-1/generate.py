
#!/usr/bin/env python3

TITLE = "Пассажиры. Часть первая"

STATEMENT = '''

НЕСА проводит очередной набор исследователей в свою космическую команду. На текущий момент уже готова система для подачи заявок, и разработчики из НЕСА рады поделиться её прототипом!
Для того, чтобы зайти на сервис, необходимо указать токен вашей команды.
Токен: %s

'''

task_ids = ["Rk8d0uJ65VjfJRlSDlkw", "vjZudBZxUeGzQDaipaHq", "k8oQkMc9RZ0qn4OtDJZY", "iBVJKVwkUrcprvSrVY5m", "ERh1V6fs84fBKNLFh2OX", "LgegDhzshj3t5AqFdcCH", "J0obOOBunbmFKRfTUD8z", "0sH0pwjQ7gmBL3Ii8tPb", "oEMbPHPKHE6PeZNfuOXm", "82EfOqvqcGmWzYVjHILB", "AInAWqglsrDp9cKzIOfS", "StSk2AMmsOac25nnYftx", "Ez94BQHsS1C3zEcqM7Ue", "kBr4xAaQBo4VF1oWi2z2", "PfyvG87xY9YkkSjXcaWW", "tbokeu207Z7usHAA48mU", "O5W3HM7rOm1tRAk6ZJOU", "c2yUrRJpLupxfXpgzZdY", "x3GB2qTxrH4ElijpOsnJ", "2IIz5IiuBAA5HyLo6y2A", "cZBqMOgmwlThSPi6xEtY", "RyKLg0VQqk2KxQvQo79V", "YAprravDMjXc7bF5KyL7", "Ix81LvZnl9DYUmlxViRu", "B442kgECeCPjl1MKiH4C", "dRovT9kKEe1zxfJGI0oE", "xnjFyeIezhxJUnpFbzHv", "xU13DuQfvIDPSbtQq3Cj", "Rjlwbiuc30IYDAdkHbuT", "1w16GW7F4mnK5W4gQ3XM", "iY3BuLqFokyNWYz8SMzl", "RWe4s4gDKTgGci1VARvL", "ZQQ16zbpOBHWdTuprCvk", "GLWvL26p4qcbkE8TRWVq", "BwarTUpsL1Ip5sqVWCCy", "5SRvLmDoG6Dy66nLK8vb", "UNkzqCab7XTW3xkhkk01", "vAEUjLcPclBpERH5AGCn", "UduoZqi2xBwMylVaaVeW", "9NfDLj8RLtXkOUTb9GCD", "YWIAgOeYgK4oN1a5UQLF", "inOSQ3dT8EhPyQeEV3Nl", "CiM9dx6LMIZSS6wUFA8n", "F7t72sEWwia6Y1XIhXsH", "wOz9YAnoHWj8Osiadop5", "Z7GPzsMAc9fYal22nAoZ", "Gn2qZdieGMtL5CIx4QSd", "BKuCRFejA9mbkmcsXcVM", "x8TR2FANKNsnI1uQI8Ln", "RaCYkWCgT6geCSUg2DsI", "igILlxDFNOCMx4uUPmup", "HYBMSspxw9KvWvfQVxJz", "meCoOqKWjpiBgTdVcvgX", "XAdfMfpZj6xn4l3EZyud", "eUBD1mdCMH5G9GEHEGQR", "maKKPAevLJjMxuarjCBX", "ucFyomybVik7CGmsDDsB", "YlOv1NJZwVlsotw0Q9ai", "BLP8gtj8QMgQIn5y9wkn", "bI01YopHZE9lrmcF3t1U", "7DEbRn31PrFRkgdxuSdX", "CDi68EOUJlYHRFUCjh3E", "1tIOV2KdZlk4DYgDxeWX", "yPSiEQ5ercwZAvqiAK4v", "eqwWo2EigWCq41PZq0x5", "DtwFLnIdKJGHAfvAWFxP", "0EpMSRwErJJMj3l4uWIJ", "XvamO6AzB2XXuZK9FJrJ", "4Uvas5wfp6P3SCmCmrXv", "efbETZb2gniTLbV1Qg3Y", "W34oMIruaX6Y5Zda3D62", "PLTZsH1Q2LUEnmPQLsSB", "gaCxp8MgIqymrd0QALJe", "Zt9CuCZbtDO8ern9rN2f", "D5to8vXC5iHmY2rLIjxK", "7vVATlOVVnmyfIZ7WDqc", "fbZzkKfXDPDvv9ay751A", "XfszIapLcqV1NZxG6o0z", "LmfEeGDx0tPoYyI2zAGW", "fQm1FwELFFrFjMUVyl6x", "q1UE0UtSN7mkYu7ozSKf", "oFXzbjqybiDfmVgqsxY6", "DhI4omWZKeyV44lp3t51", "np14PyicJbYtITPofaAa", "ez4I70ML1EmEXTOV7Zea", "g3Xxg8NG7FhjQQ6f2WB6", "AhB1Zc3chre1BHgWwQ7K", "LTMysFg6tEcDBIfOru0W", "5Lk5OxivtJAxR8KdQLBL", "yHOM9Jz8REsEWvqNPUnv", "nVFf9Ahcepxw8P5Vu60w", "PmTWUVJSytnyvtsSDbZP", "2lH6XJpUD2fg8nuTaYuG", "mx4CcVAMt498EksqbzvN", "cFe9pUiMuL6lbAf5Lesu", "7jUP4xLgKRj12QrYZxDw", "cPh3CRuJhyABlQgiqn7n", "jde3BhKgTbns5QbpIpPb", "Mj754o0ZvKoDOBA8FFCX", "0uK6OHKBaJnUyi23W5sO", "kSvhg54iaI9f2T3HdgdL", "UmdtaFv2oWUm87Et7buD", "XSzyIqusrMN1owyawhyL", "pvKzdO1nQ4CzltIGjCkg", "nQz8F4P9jhQl56stSKi8", "Jp5kAzgVglI3glRv0E4J", "nMUiKoBkJVprfo5JYl4M", "6St2hs1dKj7jdfykcQkR", "fmA0N1YkuvN7vHzy2xey", "cRXseil4PBecnjWbSllf", "uD8ZbUtGJfb9Ayk3dvWf", "aPNOfPfeEAMChXXAmMaQ", "inNPf1PyCkbwYaRARPRI", "NUE0SoUCMijzVdPrKsZb", "LLKKh7xHfFcTg92jfeW2", "5d2Co5fJyUrkXpnfNycj", "Kc4VCLpxZuH8YCSRCaNy", "1pAkQS72NbHomYaQ7bQ0", "Oxp5PILWL1TQsaWDAWXQ", "P9VkcvIUYDD6ypJMAG8v", "9seCd6RIURLZFaKfTjKu", "TNxZfAnFYMHeQAxHxM8e", "cEeZfvItrmDBc9UUQXtv", "Ti7qcRF0PcZ9ZowMcz5s", "yjZUtM6i2ZxDXPPe9Z5Z", "Peq6rtkGkprhSi15HeVc", "K4puDyBLBlji0DEzQP3S", "LSGtgj2RNmJuoXlb9VeQ", "Tu1eWddTwrjiYB6AY5mH", "7ROGDIRWF7HVHeZJYrfQ", "QRCXK7uUtJDqYvi1iF3R", "3H30RSgn8DFfbrOwhHS4", "uZKYsD0zb8atJ6utrrXB", "FYYvddVM1COjdqH3vjgS", "wWW9gXzowxXjIVRpe82K", "bVqQPcfHbLwtSbVluckL", "6rjBBfTaG4JXm1Eg79WW", "2SIPPzv0S7mekxQ1bQVe", "HuHTyDfaapN7h6OkxEIQ", "S1YGb8EsK4XDr02d0jDR", "hhJQ4ifjg0qd6QX8evhA", "WwFbar3vbuPbimSnzoNu", "BGgd3bxtsxrVUrATf32i", "yngfKE3UQecCizQkxZa0", "D0v34I64pzTHBSRnAPMy", "l0bXnx6UeAWB592hijrb", "ET3e05EqjXmXxdzBKM6S", "a0eLRyOdLsEEwpIQlljk", "uQ2Uh1aWUFjwoBUkNJdC", "rghNyL18sFlB4YWU2Qdk", "JHx7HFywjyvKR8KLEnQ0", "N9hEEhzjgiF7FDNVkaw9", "fyhYx6sKq7ck5CuwPu9I", "jBc6DuOH6L149NXUYnCh", "nEWnjohV58dSFd80RlDe", "N9vnO6LjF6HN79TI4CNr", "fZzsJnjiaLWb4Sm3csJu", "AGY4tmNBG3n75iyzBjC7", "jL0FC7aWQik1LcRo0wS1", "oECGtSeBBGp0VG9ytTGK", "f1e2MI4JRB2kXMquUeZ3", "ApNHo8ebPwpoGVJbimwm", "3RAE0Sdco5aw4o3nDWbE", "bzxtaABcHobJGxDhGnjk", "H4ydVgAlYDfZXqcjZuvY", "RBZkWDYUP8EawyG1ZkCn", "xOn58jkrh0YgctwzsKa7", "a5UK5yoSehEMrufPNDGO", "XcxTOutjR3dQszmWsCrY", "MIajVsv07I8d5FRaQsHy", "tdSKvvYLedoTwA8GkrLa", "55h6CySRPDEC6FJ67j39", "DrXlodzkooUMKhU99HNk", "GoxwNEu7d0HbQrvAwets", "3Q6JpRY544jIAi2mpEMu", "FGepCIcVYDZetQJzk0hN", "N5rqLtPOcfFnqYj2K94x", "w7ulGsLD67phzvbWVR8r", "l0zzVNxvu7fS5HeWMVAb", "k5K25CfkJuH7d1Z1Ct1Q", "oMCXipf6Uo9SHVJrdtXm", "Rq0BMMebmYDvum8HyKsi", "tmzHh3gzlF1VvcMLweRx", "Dkwed8e4PV5khvCx3sX6", "cfo05gL5AHM2Qcgd3xbY", "22W0Dohiyf6sxc933kTw", "SungFAqvxyAZ9O9IbD6N", "rRBeMHeNVGYPovNQREVQ", "2wH343rXx8r9iZA7JdVj", "0maafEzqHRgxT80OLtTr", "uOB76WeogwYAuTyVCBeB", "R5UGTunZjg5bAa9IAAqK", "ply66ns6YwTcR47IJJbN", "z9rYzvD8geVKiCODNWe8", "pon1UJGNmZX1phJG9wJl", "sMljNZqQMjmO3e7JceDk", "ne007En0zE8zT1IucKoe", "E5gH4LtShIqS6EfPFtnE", "oHC8Uo8TOebo5j1DDdIC", "gTU6njuFFxnoYy0hYqyR", "AohEXE6mPsVXRgogxfjs", "fSSTv4L87qAzOypBIkal", "lFQGfiM962mxwYII9sOE", "ne18a3jtb8Vy9v16GnyN", "n6NJ131docJHqo2Bsuqj", "Iq4KR15oTVxyE7WdvidF", "ZAgY2OA0OQ9QIqPaQr6X", "FG3IL8RK8p1BJXJCbpbx", "rPpefBqupLtBVm6GRngl", "JxDdivPQ0dAP0OlbK0wb", "4LBbhsFqjtXOxx9jq7Gh", "V10F3pgZj9l3ffgbfWJ8", "BHi29fCH5BJphet6NihN", "o6zXAvYTcPU7SadzJwhX", "kda8obo2Eogh0V4PXy0g", "FRXolP5f91UBqS1LbbXT", "bFkRySFMmG1GnnS0wK5N", "hTa8X1yvTVOFyawdl1eg", "c0yDpq1Y3rBhoFH6ENEh", "X6TKpZjFg2cn5ayH16IS", "IqGfmGm9I9oXThsmZXwp", "dGv5OO5sDD8h8suk05xc", "IctITEDghLYxdPyrcRz3", "0yywGUuoDgDvTkWnOMyc", "WkCFvA4eHMLW50Kypl5t", "O8qMlDT0cNNkdWe60BGk", "WxQTroT3UvLzU2MsvXQe", "3NkKs6v2bgM207yokCcy", "jbY8jXmdscrO0dFQVC6q", "UwcHkp4rHTwdjIxzbkiV", "KwANQsol0Pzc1wtKrHTJ", "HzmHNn9JBWUNMN7JXYpI", "BB1irRnsnJRUSEmAc463", "gVaL7omF0V9DBWt3AcxJ", "6ydAr3leh5UxRwJFumQk", "DfaLlb39lCn1QVUAjNoh", "NjRqiLm0RMpoV3J2DPxh", "o1XOeD0E2TbhqWPfTCZB", "asmGHLbxtyqIoJ5XizP3", "j3Ma6F3EHBl2YxbmAf0t", "ag80uuBK1Xv8yblIX7mP", "kxzfybKMRj99C4wknKHZ", "gUxiRPrL7tToXN00NUSG", "LTMuYRp3hCzMEJf2bRKl", "8wsSbrYK14gBXnzwWeVV", "p8eQXnT4Yx9mIAp6Qhhe", "XeSwcs8Sim6bLl9wM7d1", "OebuHlTF28qPgzRnfrAM", "CMPeScgb9AHS7v9Isham", "Hg1jkbRQGUmbO6jmCUV6", "oGeLBxYIeHkYH5OfFqhB", "3XIvrwXNteerUYsUxnVi", "mFKDzgr6lTyXCzexbaNF", "4Qa4ZkKuPLUGwKVhV40K", "kny8MlEqzWp32062HtIE", "zxIeNx5hzKJLLixkiier", "cTJVe0s7UzXkEcqLu1Al", "UkNValPy64ivtOrhPv01", "vApbiV9qNBBTFtwKF8yf", "Fx1GIO5ILyaRlfaysLwu", "yGE0XWYZBkcY77ahMmas", "RWXORieIOSX9T8dK4DAv", "dOyl42udeJLDvVmIpfVY", "ShoKlygmPU9wz1y3cr5F", "seVDwRYswlh9r5t74pmj", "j6pSd12oxMwuARxmmsLZ", "GNn0QRZkiKNspBoFuEfY", "V9tC4FOC5UmHAr8Y68Bo", "6lUGdbFx9pWX86uSlLcf", "l7zRHbeG7mvRJHNfmaVc", "MVH7fzN9ek7GIhqquQBl", "LElQosvBAwROa47lOwFA", "zCdmM7qznpsQkZjT8L18", "bxf1KNHzKiSZ8GSIm45T", "O79XOjdRL7SQr63TuZkw", "ax6ckyAHq2AgDcG4W2hl", "BzLMmjYcPImbVjJ3kKSO", "peujM9fUMZAGlRw93ql8", "fNhvhqIxeWwpi39dR1UK", "GWYGdvrgGAlBe5dz7FOt", "8s3Js7jNf2eY9rH7opA1", "EHSO7WUk4ZUScgG0JTeO", "bGvn5V5wMYgwJ37PauTH", "rjf19BdcB4sucsYbWOj5", "sG8Lec8FdR92Mss1IFGi", "RwVSE5BtqZsTocMgHudH", "QOCvAp3C8sFTpWDCpKjy", "KBHMgbLFDHnATarEYGTy", "PYmnkYVDhZST8ja1GjGt", "St9BjXpqZ4ukJMbs2ZQx", "CkuJLNbSVXhylhDpIX1c", "Bt9jbbhkmivSERmkWlzA", "tcFSbGz5PcKWzYCgxHuz", "8txUiXNQ3MOUkji6zS7Q", "13OcdIeqh035CW2Xxn7k", "px7PlpSJ55Ik7ti7vDre", "takA9XC64JhevTuhngIR", "3z84U8pcbNAuz4gj5ekp", "LGqVmgyrRH2OsiOVF2jl", "Ng8WlCBkjRwHm17Bdagx", "Zfqxl5AZygvY7P0a0peT", "8tbZVgZRHbx742nelnDv", "XNG7EzJXaNuIPIl1ulTW", "NBVCUVkAS0zg1prZf3Ni", "t5zxHbtPDSIoaXVn1Bxy", "KOw6UyGAAQ9s7t2X7wTu", "z8CBXvUoSTDDcLhgWAIU", "B8dibwe7C0kRW7gezwMq", "VC12abESMp626MFGNinv", "abGgfrAZ4raHzkJpu0GW", "CLnjzXb96qbs5vd1Su0f", "hLmj358vABwNCNvBUBVq", "wGfH2FyrKxw5otoFaYOQ", "DFR152f6Li9NJgOR57tT", "CLV31FtiRCujiPVqxTaL", "CAMJDWPzS2MOsB400uHG", "9hHNu4OHr8NyKHSqC2Pp", "hCp118nEFwMyqPy8hm8I", "9IAJ1drkvlMwAp8piVaH", "ed6CXb0eiqmz0y8j1Sx4", "ks5QtESfu5cEKNve7LwO", "38s3Jex4jxVjk92RtXZh", "xEL40F7PK8cFAWjkE9ec", "2lBHvIox6LwcWtJPi6iX", "vDu8j7qCDfRu5mm93rp2", "RtS7duONGrKQFLjQWMWB", "lv2jOnYSls055yGuKJbO", "XK4pYuEFxFkIGhvorGub", "CHEPDgS1xqQbkWfULnXa", "TRUfm3o4zfwYqgbMPNbk", "lbzMLllPOn3Bz1MUDcV6", "Szt1VLcPpWj8PL6p3UOJ", "mmtxeFenqzYDMKsX7xpT", "cnKjKcXBBjNDIjqMblOa", "8MrVTVzRfMmhSjwpNN6f", "HSqF1Ds4asGTnHZpHh3J", "SNP8EQheYTenTkwbKBoS", "ZzmT5RY6548RDR5GF14h", "162BI80wNwjRyqlLGOvL", "8hbEE1j9IdjeRSc9mOI8", "mDRHQ4YqEb5KGJMSttvX", "dQqXLV5WRpCwfTTk1fm6", "LFjVTCzqs83PaHR9LSKF", "hExPvZevB6iTe2tD2kwc", "KJNb2ejjD7YmnVVXCFQF", "43LEBPvSXRyI7Bdn7F8m", "TDUgBpHcJ8M5dJgSMPbU", "C0CrazfGCOoGsqZxPIIt", "nMBNXEzUWQLHbZF3GmCs", "2JnJaGYBtnKiXCKjFOMZ", "qYRVsxGHcXkmqL7VtXau", "xjn6tKjfFD6DRlyQ9wVY", "pOGO4a1nLK8iCLI4o21D", "qHb2sWMdtP3IRmHDA4Td", "Jkyre6r65tFyMBPHXX5S", "MZRVynHFIaf18CCxoNwI", "qqlT7eswtH1jYA84jIbo", "6FclIQI9JpI2mqSzW8Q8", "zqqfHkVzXeCylUNpWuX4", "Rg9BgI1fMV5lMgdqlepl", "CG0QlBLykqsAPPoDvjlF", "FwoC8jsHm94KERbd3aeG", "1ba4f7momTllIyrUJeC0", "dV5gnIfKOnuBGyoUWLPc", "bwbd1xhwJ4ejqat0vouP", "LgtLJczcJLrQJMljZAZo", "slvmuUFnP2nnl27EogO9", "20ZGZtxk2sIiWUmLmnpD", "HePYKK0sHNXsg5AjH8uK", "KJL7YwvRvy0NZBkEL6pI", "z9983QWF6XIp8uB1KGXr", "Yxec7n2rLGju6pZ8PtVT", "EOjHiAjg2SeEjRjrbAf4", "G4QDVSApVCV4QdI7DAf7", "dDT30HDpmT7pbw8KTXp4", "OLrjQvVe8qKE8FevBHq0", "FzFgRRDjYvG4Nx2uZkWk", "Yp7rt9WiMHn44JzDGmBb", "0pZTg8AxTKd8BWBrX77e", "vWwiehpvFLmJ19IBPlca", "I5cr6ca9N9Evtajkuvf5", "pgq8mIKr6dDBW4vxRyIP", "WHwzfstjxIN8upjO0AkF", "VZ4hJPrmXeu4pQa6PGoD", "jStoNhtJDdZVeLW32FnV", "2Pnh1qzqNoWJXQTzOlSm", "AToV75LidpVmANgJr0Uk", "Ta6XWBRrDWmd8GaGSakO", "0GJLZgPrD3JXm7vfOpKC", "8Qx8uIJsjJXKVbkFoedB", "D2OaVruRXHO7zmqe6Ajq", "T0yhZule0lUzRFRUaKAQ", "6AUM9GbxizA3tIXeLoag", "QTzTYJLobGyxRQLdMOPf", "c9dAaHmlNuYqJQrTu5mt", "Pf63ugaepw5RbVOCwVFd", "KaINmfVlDxEeLgB6cW4X", "X8WAPoCw5adj5GCW9PkP", "JksIUJd5J0lga65CaxYc", "423Ps19rWgS2HsQyqP33"]


def generate(context):
    participant = context['participant']

    task_id = task_ids[participant.id % len(task_ids)]

    return TaskStatement(TITLE, STATEMENT % task_id)
