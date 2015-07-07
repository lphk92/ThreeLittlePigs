from ascii_art import AsciiArt
class Fire(object):
    def __init__(self):
        self.art = AsciiArt(fire_str)

    def __str__(self):
        return str(self.art)

fire_str = """









            (  .      )
        )           (              )
              .  '   .   '  .  '  .
     (    , )       (.   )  (   ',    )
      .' ) ( . )    ,  ( ,     )   ( .
   ). , ( .   (  ) ( , ')  .' (  ,    )
  (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
"""
