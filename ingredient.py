ó
B-Rc           @   s   d  d d     YZ  d S(   t
   Ingredientc           B   sk   e  Z d  Z i  d  Z d   Z d   Z d   Z d   Z d   Z d   Z	 d   Z
 d	   Z d
   Z RS(   s$   A liquid ingredient of a mixed drinkc         C   s   | |  _  | |  _ d S(   sL  Returns a new Ingredient instance.

        Keyword arguments:
        flavs -- dictionary of string keys, the flavors, and number values:
            name -- string, name of ingredient
            sweetness -- scale of 0 to 1 (default 0)
            proof -- 0 to 200 (default 0)
            bitterness -- scale of 0 to 1 (default 0)
            sourness -- scale of 0 to 1 (default 0)
            flavorStrength -- how flavorful in general, scale of 0 to 1 (default 0)
            carbonation -- scale of 0 to 1 (default 0)
            creaminess -- scale of 0 to 1 (default 0)
        N(   t   namet   flavors(   t   selfR   t   flavs(    (    s!   /var/RobotBartender/ingredient.pyt   __init__   s    	c         C   s   d G| Gd G|  j  GHd S(   sk   Print the adding of an ingredient

        Keyword arguments:
        amnt -- amount to add, in mL
        t   Addings   mL ofN(   R   (   R   t   amnt(    (    s!   /var/RobotBartender/ingredient.pyt   add   s    c         C   s!   |  j  j |  r |  j  | Sd S(   sy   Returns the value of the flavor, 0 if no value

        Keyword arguments:
        flavor -- string, flavor name
        i    (   R   t   has_key(   R   t   flavor(    (    s!   /var/RobotBartender/ingredient.pyt	   getFlavor   s    c         C   s   |  j  d  S(   Nt   proof(   R   (   R   (    (    s!   /var/RobotBartender/ingredient.pyR   &   s    c         C   s   |  j  d  S(   Nt	   sweetness(   R   (   R   (    (    s!   /var/RobotBartender/ingredient.pyR   )   s    c         C   s   |  j  d  S(   Nt
   bitterness(   R   (   R   (    (    s!   /var/RobotBartender/ingredient.pyR   ,   s    c         C   s   |  j  d  S(   Nt   sourness(   R   (   R   (    (    s!   /var/RobotBartender/ingredient.pyR   /   s    c         C   s   |  j  d  S(   Nt   flavorStrength(   R   (   R   (    (    s!   /var/RobotBartender/ingredient.pyR   2   s    c         C   s   |  j  d  S(   Nt   carbonation(   R   (   R   (    (    s!   /var/RobotBartender/ingredient.pyR   5   s    c         C   s   |  j  d  S(   Nt
   creaminess(   R   (   R   (    (    s!   /var/RobotBartender/ingredient.pyR   8   s    (   t   __name__t
   __module__t   __doc__R   R   R   R   R   R   R   R   R   R   (    (    (    s!   /var/RobotBartender/ingredient.pyR       s   		
						N(    (   R    (    (    (    s!   /var/RobotBartender/ingredient.pyt   <module>   s    