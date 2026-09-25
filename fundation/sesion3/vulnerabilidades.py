vulnerabilities = [
	{"name": "SQL injection", "severity": 9.8},
	{"name": "Cross-site scripting", "severity": 6.1},
	{"name": "Weak password", "severity": 3.7},
]

vulnerabilities_sorted = sorted(
	vulnerabilities,
	key=lambda vulnerability: vulnerability["severity"],
	reverse=True,
)
