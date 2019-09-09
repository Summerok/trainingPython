# -*-coding:Latin-1 -*
def controler_types(*a_args, **a_kwargs):
    """On attend en param�tres du d�corateur les types souhait�s. On accepte
    une liste de param�tres ind�termin�s, �tant donn� que notre fonction
    d�finie pourra �tre appel�e avec un nombre variable de param�tres et que
    chacun doit �tre contr�l�"""
    
    def decorateur(fonction_a_executer):
        """Notre d�corateur. Il doit renvoyer fonction_modifiee"""
        def fonction_modifiee(*args, **kwargs):
            """Notre fonction modifi�e. Elle se charge de contr�ler
            les types qu'on lui passe en param�tres"""
            
            # La liste des param�tres attendus (a_args) doit �tre de m�me
            # Longueur que celle re�ue (args)
            if len(a_args) != len(args):
                raise TypeError("le nombre d'arguments attendu n'est pas �gal " \
                        "au nombre re�u")
            # On parcourt la liste des arguments re�us et non nomm�s
            for i, arg in enumerate(args):
                if a_args[i] is not type(args[i]):
                    raise TypeError("l'argument {0} n'est pas du type " \
                            "{1}".format(i, a_args[i]))
            
            # On parcourt � pr�sent la liste des param�tres re�us et nomm�s
            for cle in kwargs:
                if cle not in a_kwargs:
                    raise TypeError("l'argument {0} n'a aucun type " \
                            "pr�cis�".format(repr(cle)))
                if a_kwargs[cle] is not type(kwargs[cle]):
                    raise TypeError("l'argument {0} n'est pas de type" \
                            "{1}".format(repr(cle), a_kwargs[cle]))
            return fonction_a_executer(*args, **kwargs)
        return fonction_modifiee
    return decorateur

@controler_types(int,float)
def intervalle(borne_inf, borne_sup):
    print("les limites sont min: {0} et max: {1}".format(borne_inf, borne_sup))


intervalle(3, 5.32323231)