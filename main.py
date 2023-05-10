from flet import *


def main(page:Page):
   
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"    

    
    def ganti(e):
        ctx.bgcolor ="blue" if isLogin.value == "Login" else "red"
        ctx.height = 500 if isLogin.value == "Login" else 150
        ctx.width = 300 if isLogin.value == "Login" else 200
        ctx.border_radius = 0 if isLogin.value == "Login" else 100
        
        isLogin.value = "Register" if isLogin.value == "Login" else "Login"
        isLogin.offset = transform.Offset(5,0) if isLogin.value == "Login" else transform.Offset(0,0)

        isRegister_btn.value = "Register" if isLogin.value == "Login" else "Login"
        isRegister_btn.offset =  transform.Offset(0,0) if isLogin.value == "Login" else transform.Offset(5,0)

        txt_box_register.visible = True if isLogin.value == "Register" else False
        page.update()



    # formulair registzer

    txt_box_register = Container(
        content = Column([
            TextField(
                label="Username",
                border_color = "white",
                color = "white"
                      ),
            TextField(
                label="Password",
                border_color = "white",
                color = "white"
                      ),
            # Login button elevator
            ElevatedButton("Login",
                width = page.window_width,
                bgcolor = "white",
                color = "blue",
                on_click = ganti
                )
            
            ])
        )

    # set register hidden
    txt_box_register.visible = False
    

    isLogin = Text("Login",
                   weight = "bold",
                   color="white",
                   size=20,

                   #animation this
                   offset = transform.Offset(0,0),
                   animate_offset = animation.Animation(duration=300)
                   )

    isRegister_btn = ElevatedButton("Register",
                                    on_click = ganti,
                                    #animation this
                                    offset = transform.Offset(0,0),
                                    animate_offset = animation.Animation(duration=300)
                                    ) 
   

    ctx = Container(
        bgcolor="red",
        border_radius = 100,
        padding = 20,
        width = 200,
        height = 150,
        alignment = alignment.center,
        animate = animation.Animation(duration=300,curve="easeInOut"),
        content = Column([
            isLogin,
            txt_box_register,
            isRegister_btn
            
            ])
        )

    page.add(
        ctx
        )


flet.app(target=main)