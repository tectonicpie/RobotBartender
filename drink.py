�
D-�Rc           @   s   d  d d �  �  YZ  d S(   t   Drinkc           B   s,   e  Z d  Z d �  Z d d � Z d �  Z RS(   s4   A mixed drink with a list of ingredients and amountsc         C   s[   | |  _  | |  _ d |  _ x' |  j D] } |  j |  j | 7_ q% Wt |  j � |  _ d S(   s�   Return a new instance of Drink.

        Keyword arguments:
        name -- string, the name of the drink
        ings -- dictionary of Ingredients (keys) and no. of parts (value)
        i    N(   t   namet   ingredientst
   totalPartst   float(   t   selfR   t   ingst
   ingredient(    (    s   /var/RobotBartender/drink.pyt   __init__   s    			id   c         C   sM   x6 |  j  D]+ } | j t | |  j  | |  j � � q
 Wd G|  j Gd GHd S(   s   Print the actions of making a drink

        Keyword arguments:
        size -- int, size of drink in mL (default 100)
        t   Yours	   is ready.N(   R   t   addt   intR   R   (   R   t   sizeR   (    (    s   /var/RobotBartender/drink.pyt   make   s    )c         C   s�   | d k r d } n d } | Gd G| Gd G|  j  GHd } x/ |  j D]$ } | | j | � |  j | 7} qC W| |  j :} xu |  j D]j } |  j | c | | j | � | | 7<| j | � | | d k r� d } n d } | Gd G| j  GHq� Wd S(   s�   Alter the ingredient ratios to increase or decrease a flavor

        Keyword arguments:
        flavor -- string, the name of the flavor to alter
        amount -- how much to alter it. Range -1 (less) to 1 (more)
        i    t
   Increasingt
   Decreasingt   thes   of thes   the amount ofN(   R   R   t	   getFlavorR   (   R   t   flavort   amountt   changingt   levelR   (    (    s   /var/RobotBartender/drink.pyt   alterRecipe   s    	"(	(   t   __name__t
   __module__t   __doc__R   R   R   (    (    (    s   /var/RobotBartender/drink.pyR       s   	N(    (   R    (    (    (    s   /var/RobotBartender/drink.pyt   <module>   s    