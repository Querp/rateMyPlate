WAAROM
    class based views?
    meerdere apps? (url namespace?)

VIEWS
    make user/player (guest)
        add User
        add Player
    change competition (admin)
    delete competition (admin)
    join competition (player)
        add PlayerCompetition
        add Satay
    rate satay
        add Rating (taste, tenderness, comment)
    change rating

CUSTOMISE USER REGISTRATION
    add e-mail(optional or not? required for reset)
    add player name(default username or required at registering?)


let organiser invite players
render dateTime model form as <input type="datetime-local">
add database changes log
auto login after registering?
competitie afbeelding placeholders
login msg, welcome {{ user.username }}
remove trailing space form inputs with default value (competition name)