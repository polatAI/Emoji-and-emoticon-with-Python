import turtle

emo = turtle.Turtle()

# Emoji'nin yüzünü oluşturacak olan dairenin merkezini belirlemek için (0, -100) konumuna gidilir.
emo.up()
emo.goto(0, -100)
emo.down()

# Daire içini sarı renkte doldur.
emo.begin_fill()
emo.pendown()
emo.fillcolor('yellow')
emo.circle(100)  # Dairenin boyutu
emo.end_fill()

# Gülümseme çizmek için yarı çember oluştur.
emo.up()
emo.goto(-67, -15)
emo.setheading(-60)
emo.width(5)
emo.down()
emo.circle(80, 120)
emo.fillcolor("black")  # Gülümsemenin siyah renkte olmasını sağlar.

# Gözleri çizmek için döngü oluştur.
for i in range(-35, 105, 70):
    emo.up()
    emo.goto(i, 35)
    emo.setheading(0)
    emo.down()
    emo.begin_fill()
    emo.circle(10)
    emo.end_fill()

emo.penup()
emo.goto(0, -150)  # İmleci alt kısma taşır.

# Ekranın açık kalmasını sağlamak için mainloop kullanılır.
turtle.mainloop()
