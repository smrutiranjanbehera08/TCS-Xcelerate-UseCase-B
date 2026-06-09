from session_manager import SessionManager

session = SessionManager()

session.save(
    "last_company",
    "TCS.NS"
)

session.save(
    "last_sector",
    "Technology"
)

print(session.get("last_company"))

print(session.get("last_sector"))

print("\nFull Session:\n")

print(session.show_all())