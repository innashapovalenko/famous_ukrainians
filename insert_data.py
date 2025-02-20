from flask_ukrainians import app, db, Human

with app.app_context():
    human1 = Human(name="Taras Shevchenko", 
                 poem="Заповіт (Testament)", 
                 biography="Taras Shevchenko was a Ukrainian poet, artist, and national figure.")
    
    human2 = Human(name="Lesya Ukrainka", 
                 poem="Contra Spem Spero", 
                 biography="Lesya Ukrainka was a Ukrainian poet and writer known for her strong national identity.")
    human3 = Human(name="Pavlo Tychyna", 
               poem="Арфами, арфами (With Harps, With Harps)", 
               biography="Pavlo Tychyna was a prominent Ukrainian poet, a master of symbolism, and later a public figure. His works are characterized by their vivid expression and lyrical beauty.")

    human4 = Human(name="Volodymyr Sosiura", 
                poem="Любіть Україну (Love Ukraine)", 
                biography="Volodymyr Sosiura was a Ukrainian poet and writer, known for his passionate love for Ukraine. His works often explored themes of national pride and the hardships of the Ukrainian people. 'Love Ukraine' remains one of his most famous poems, celebrated for its deep emotional resonance.")

    human5 = Human(name="Vasyl Stus", 
                poem="Як добре те, що в серці є (How Good It Is That There Is In the Heart)", 
                biography="Vasyl Stus was a Ukrainian poet, dissident, and human rights activist, known for his deeply philosophical and emotionally charged poems. His works reflect his fierce love for Ukraine, its people, and its language, as well as his struggle against Soviet oppression. Stus was imprisoned for his views, and he is considered one of the most important voices of the Ukrainian resistance.")
    db.session.add(human1)
    db.session.add(human2)
    db.session.add(human3)
    db.session.add(human4)
    db.session.add(human5)
    db.session.commit()

    print("Data inserted successfully!")
