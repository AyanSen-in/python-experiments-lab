print("""      SIGN UP
                   │
                   ▼
        User enters username/email/password
                   │
                   ▼
          Validate the information
                   │
         ┌─────────┴─────────┐
         │                   │
         ▼                   ▼
       Invalid              Valid
         │                   │
         ▼                   ▼
    Show error       Check duplicates
                             │
                             ▼
                      Hash password
                             │
                             ▼
                      Save user data
                             │
                             ▼
                       Account created


                 LOGIN
                   │
                   ▼
        User enters username/password
                   │
                   ▼
            Find the user
                   │
          ┌────────┴────────┐
          │                 │
          ▼                 ▼
      Not found         User found
          │                 │
          ▼                 ▼
       Reject       Verify password hash
                            │
                    ┌───────┴────────┐
                    │                │
                    ▼                ▼
                 Wrong             Correct
                    │                │
                    ▼                ▼
                 Reject         Login successful   
                 
                 
                 
                 
                 """)

