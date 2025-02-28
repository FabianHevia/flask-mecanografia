from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Base de datos de citas (podría moverse a un archivo JSON o base de datos real)
QUOTES = {
    "es": [
        {
            "text": "En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor.",
            "author": "Miguel de Cervantes"
        },
        {
            "text": "La vida no es la que uno vivió, sino la que uno recuerda y cómo la recuerda para contarla.",
            "author": "Gabriel García Márquez"
        },
        {
            "text": "El amor es una amistad con momentos eróticos.",
            "author": "Antonio Gala"
        },
        {
            "text": "La música es el arte más directo, entra por el oído y va al corazón.",
            "author": "Magdalena Martínez"
        },
        {
            "text": "La creatividad es la inteligencia divirtiéndose.",
            "author": "Albert Einstein"
        },
        {
            "text": "El misterio de la vida no es un problema a resolver, sino una realidad a experimentar",
            "author": "Frank Herbert (Duna)"
        },
        {
            "text": "Estar solo no tiene nada que ver con cuantas personas hay alrededor",
            "author": "Richard Yates (Revolutionary Road)"
        },
        {
            "text": "Sea un hombre o sea más que un hombre. Sea firme con su propósito y firme como una piedra",
            "author": "Mary Shelley (Frankestein)"
        },
        {
            "text": "El hombre débil se vuelve fuerte cuando no tiene nada, porque sólo entonces puede sentir la locura de la desesperación",
            "author": "Arthur Conan Doyle (La compañía blanca)"
        },
        {
            "text": "Si buscas la perfección nunca estarás contento",
            "author": "Leo Tolstoy (Anna Karenina)"
        },
        {
            "text": "Mientras el corazón late, mientras el cuerpo y alma siguen juntos, no puedo admitir que cualquier criatura dotada de voluntad tiene necesidad de perder la esperanza en la vida",
            "author": "Julio Verne (Viaje al centro de la tierra)"
        },
        {
            "text": "No puedo morir aún doctor. Todavía no. Tengo cosas que hacer. Después de todo, tendré una vida entera en la que morir",
            "author": "Carlos Ruiz Zafón (El Juego del Ángel)"
        },
        {
            "text": "Tengo esperanza o podría no vivir",
            "author": "H.G. Wells (La isla del doctor Moreau)"
        },
        {
            "text": "Llamo a la gente “rica” cuando son capaces de satisfacer las necesidades de su imaginación",
            "author": "Henry James (El retrato de una dama)"
        },
        {
            "text": "El sol es débil cuando se eleva primero, y cobra fuerza y coraje a medida que avanza el día",
            "author": "Charles Dickens (Vieja tienda de curiosidades)"
        },
        {
            "text": "Es en las noches de diciembre, cuando el termómetro está a cero, cuando más pensamos en el sol",
            "author": "Victor Hugo (Los miserables)"
        },
        {
            "text": "Cada libro, cada volumen que ves aquí, tiene un alma. El alma de la persona que lo escribió y de aquellos que lo leyeron, vivieron y soñaron con él. Cada vez que un libro cambia de manos, cada vez que alguien baja sus ojos a las páginas, su espíritu crece y se fortalece",
            "author": "Carlos Ruiz Zafón (La Sombra del Viento)"
        },
        {
            "text": "Mi consejo es: nunca hagas mañana lo que puedes hacer hoy. La procrastinación es la ladrona del tiempo",
            "author": "Charles Dickens (David Copperfield)"
        },
        {
            "text": "Luchar hasta el último aliento",
            "author": "William Shakespeare (Enrique VI)"
        },
        {
            "text": "Conseguir lo que quieres es tan difícil como no conseguir lo que quieres. Porque entonces tienes que averiguar qué hacer con ello, en lugar de averiguar qué hacer sin ello",
            "author": "David Levithan (El reino de la posibilidad)"
        },
        {
            "text": "Deja de preocuparte por envejecer y piensa en crecer",
            "author": "Philip Roth (El animal moribundo)"
        },
        {
            "text": "Crearía un perfume que no sólo fuera humano, sino sobrehumano. Un aroma de ángel, tan indescriptiblemente bueno y pletórico de vigor que quien lo oliera quedaría hechizado y no tendría más remedio que amar a la persona que lo llevara, o sea, amarle a él, Grenouille, con todo su corazón",
            "author": "Patrick Süskind (El Perfume)"
        },
        {
            "text": "¡Qué maravilloso es que nadie necesite esperar ni un solo momento antes de comenzar a mejorar el mundo!",
            "author": "Ana Frank (El Diario de Ana Frank)"
        },
        {
            "text": "Crees que sabes todas tus posibilidades. Entonces, otras personas llegan a tu vida y de repente hay muchas más",
            "author": "David Levithan (El reino de la posibilidad)"
        },
        {
            "text": "Nada hay en el mundo, ni hombre ni diablo ni cosa alguna, que sea para mí tan sospechoso como el amor, pues éste penetra en el alma más que cualquier otra cosa. Nada hay que ocupe y ate más al corazón que el amor. Por eso, cuando no dispone de armas para gobernarse, el alma se hunde, por el amor, en la más honda de las ruinas",
            "author": "Umberto Eco (El Nombre de la Rosa)"
        },
        {
            "text": "Seas quien seas, hagas lo que hagas, cuando deseas con firmeza alguna cosa es porque este deseo nació en el alma del universo. Es tu misión en la tierra",
            "author": "Paulo Coelho (El Alquimista)"
        },
        {
            "text": "De pronto se deslizó por el pasillo, al pasar por mi lado sus sorprendentes pupilas de oro se detuvieron un instante en las mías. Debí morir un poco. No podía respirar y se me detuvo el pulso",
            "author": "Isabel Allende (La Casa de los Espíritus)"
        },
        {
            "text": "El hombre llega mucho más lejos para evitar lo que teme que para alcanzar lo que desea",
            "author": "Dan Brown (El Código da Vinci)"
        },
        {
            "text": "Nuestras vidas se definen por las oportunidades, incluso las que perdemos",
            "author": "F. Scott Fitzgerald (El curioso caso de Benjamin Button)"
        },
        {
            "text": "No todo lo que es de oro reluce, ni toda la gente errante anda perdida",
            "author": "J.R.R. Tolkien (El Señor de los Anillos)"
        },
        {
            "text": "Amor y deseo son dos cosas diferentes; que no todo lo que se ama se desea, ni todo lo que se desea se ama",
            "author": "Miguel de Cervantes (Don Quijote de la Mancha)"
        },
        {
            "text": "Cuando te hayas consolado, te alegrarás de haberme conocido",
            "author": "Antoine de Saint-Exupèry (El Principito)"
        },
        {
            "text": "Era el mejor de los tiempos, era el peor de los tiempos, era la edad de la sabiduría, era la edad de la insensatez, era la época de la creencia, era la época de la incredulidad, era la estación de la luz, era la estación de la oscuridad, era la primavera de la esperanza, era el invierno de la desesperación",
            "author": "Charles Dickens (Historia de dos Ciudades)"
        },
        {
            "text": "Y una vez disipados los malos olores del pasado, quería ahora inundarlo de fragancias",
            "author": "Patrick Süskind (El Perfume)"
        },
        {
            "text": "Me será muy difícil vengar a todos los que tienen que ser vengados, porque mi venganza no sería más que otra parte del mismo rito inexorable",
            "author": "Isabel Allende (La Casa de los Espíritus)"
        },
        {
            "text": "Se quien era esta mañana cuando me levanté, pero creo que he debido cambiar varias veces desde entonces",
            "author": "Lewis Carroll (Alicia en el País de las Maravillas)"
        },
        {
            "text": "No soy un pájaro y ninguna red me atrapa. Soy un ser humano libre con una voluntad independiente",
            "author": "Charlotte Bronte (Jane Eyre)"
        },
        {
            "text": "La mayor aventura es la que nos espera. Hoy y mañana aún no se han dicho. Las posibilidades, los cambios son todos vuestros por hacer. El molde de su vida en sus manos está para romper",
            "author": "J.R.R. Tolkien (El Hobbit)"
        },
        {
            "text": "Siento que me estoy moviendo hacia delante a la vez que alejándome de algo, y todo es posible",
            "author": "Bret Easton Ellis (American Psycho)"
        },
        {
            "text": "Si la gente simplemente ama a los demás solo un poco, pueden ser muy felices",
            "author": "Émile Zola (Germinal)"
        },
        {
            "text": "Nunca se sabe lo que la mala suerte te ha salvado de una peor suerte",
            "author": "Cormac Mccarthy (No es país para viejos)"
        },
        {
            "text": "No me gusta trabajar – a ningún hombre le gusta – pero me gusta lo que hay en el trabajo – la oportunidad para encontrarte a ti mismo. Tu propia realidad – para ti, no para otros- lo que ningún otro hombre podrá saber",
            "author": "Joseph Conrad (El corazón de las tinieblas)"
        },
        {
            "text": "Alicia: ¿Cuánto tiempo es para siempre? Conejo blanco: A veces solo un segundo",
            "author": "Lewis Carroll (Alicia en el País de las Maravillas)"
        },
        {
            "text": "Lo peor de la religión era la gente religiosa",
            "author": "Jeffrey Eugenides (La trama nupcial)"
        },
        {
            "text": "La mente hace su propio lugar, y en sí misma puede hacer un cielo del infierno, y un infierno del cielo",
            "author": "John Milton (Paraíso perdido)"
        },
        {
            "text": "Ammu dijo que los seres humanos eran criaturas de hábito, y que era increíble el tipo de cosas a las que se podían acostumbrarse",
            "author": "Arundhati Roy (El dios de las pequeñas cosas)"
        },
        {
            "text": "Ama a quienes amas mientras los tienes. Eso es todo lo que puedes hacer. Déjalos ir cuando debes. Si sabes cómo amar, nunca escaparas",
            "author": "Ann Brashares (Mi nombre es memoria)"
        },
        {
            "text": "Hay gente que, cuanto más haces por ellos, menos hacen por sí mismos",
            "author": "Jane Austen (Emma)"
        },
        {
            "text": "Hay libros cuyas partes traseras y cubiertas son de lejos la mejor parte",
            "author": "Charles Dickes (Oliver Twist)"
        },
        {
            "text": "El mundo era tan reciente, que muchas cosas carecían de nombre, y para mencionarlas había que señarlarlas con el dedo",
            "author": "Gabriel García Marquez (Cien años de soledad)"
        },
        {
            "text": "Las personas mayores nunca pueden comprender algo por sí solas y es muy aburrido para los niños tener que darles una y otra vez explicaciones",
            "author": "Antoine de Saint-Exupéry (El principito)"
        },
        {
            "text": "Cuando sientas deseos de criticar a alguien, recuerda que no todo el mundo ha tenido las mismas oportunidades que tú tuviste",
            "author": "F. Scott Fitzgerald (El gran Gatsby)"
        },
        {
            "text": "La vida cambia rápido. La vida cambia en un instante. Te sientas a cenar y la vida como la conoces termina",
            "author": "Joan Didion (El año del pensamiento mágico)"
        },
        {
            "text": "¿Sabes lo que ocurre cuando haces daño a la gente? Dijo Ammu. Cuando dañas a la gente, comienzan a quererte menos. Eso es lo que hacen las palabras descuidadas. Hacen que la gente te quiera un poco menos",
            "author": "Arundhati Roy (El dios de las pequeñas cosas)"
        },
        {
            "text": "Cuando tienes miedo pero lo haces de todas formas, eso es valentía",
            "author": "Neil Gaiman (Coraline)"
        },
        {
            "text": "Hay que tener cuidado con los libros y lo que hay dentro de ellos, ya que las palabras tienen el poder de cambiarnos",
            "author": "Cassandra Clare (El Ángel mecánico)"
        },
        {
            "text": "La amistad es sin duda el mejor bálsamo para los dolores de la decepción amorosa",
            "author": "Jane Austen (La abadía de Northanger)"
        },
        {
            "text": "Nos contamos historias a nosotros mismos para vivir",
            "author": "Joan Didion (El Álbum blanco)"
        },
        {
            "text": "Hablar sin sentido es el único privilegio que la humanidad posee sobre otros organismos. Es al hablar sin sentido cuando uno llega a la verdad. Hablo sin sentido, por tanto soy humano",
            "author": "Fyodor Dostoevsky (Crimen y Castigo)"
        },
        {
            "text": "No puedes decir “no” a la gente que amas, no a menudo. Ese es el secreto. Y cuando lo haces, tiene que sonar como un “si” o le tienes que hacer decir “no”",
            "author": "Mario Puzo (El padrino)"
        },
        {
            "text": "Otros escribirán desde la cabeza, pero él escribe desde el corazón, y el corazón siempre le entiende",
            "author": "Washington Irving (La leyenda de Sleepy Hollow y otras historias)"
        },
        {
            "text": "Si quieres saber cómo es un hombre, mira como trata a sus inferiores, no a sus iguales",
            "author": "J.K. Rowling (Harry Potter y el Cáliz, Fuego de J.K. Rowling)"
        },
        {
            "text": "Todos los finales son también comienzos. Simplemente no lo sabemos en el momento",
            "author": "Mitch Albom (Las cinco personas que conocerás en el cielo)"
        },
        {
            "text": "Las varitas son tan poderosas como las brujas que las usan. A algunas brujas les gusta jactarse de que son más grandes y mejores que otra gente",
            "author": "J.K. Rowling (Harry Potter y las Reliquias de la Muerte)"
        },
        {
            "text": "La gente encuentra mucho más sencillo perdonar a otros por estar equivocados que por estar en lo cierto",
            "author": "J.K. Rowling (El príncipe mestizo)"
        },
        {
            "text": "¿Te has enamorado alguna vez? ¿No es horrible? Te hace tan vulnerable. Abre tu pecho y abre tu corazón y significa que alguien puede entrar en ti y deshacerte",
            "author": "Neil Gaiman (Las benévolas)"
        },
        {
            "text": "La felicidad se puede encontrar, incluso en los tiempos más oscuros, solo si se recuerda encender la luz",
            "author": "J.K. Rowling (El Prisionero de Azkaban)"
        },
        {
            "text": "Por la tarde fue a ver al cine “El Señor de los Anillos”, la cuál no había tenido tiempo para ver antes. Pensó que los orcos, a diferencia de los seres humanos, eran criaturas simples y sin complicaciones",
            "author": "Stieg Larsson (La Chica del Dragón Tatuado)"
        },
        {
            "text": "Resulta extraño pensar que, cuando uno teme algo que va a ocurrir y quisiera que el tiempo empezara a pasar más despacio, el tiempo suele pasar más deprisa",
            "author": "JK Rowling (Harry Potter y el Cáliz de fuego)"
        },
        {
            "text": "Reflexionar serena, muy serenamente, es mejor que tomar decisiones desesperadas",
            "author": "Franz Kafka (La Metamorfosis)"
        },
        {
            "text": "La impresionó tanto su enorme desnudez tarabiscoteada que sintió el impulso de retrocede",
            "author": "Gabriel García Márquez (Cien Años de Soledad)"
        },
        {
            "text": "Es mejor mirar al cielo que vivir allí",
            "author": "Truman Capote (Desayuno con diamantes)"
        },
        {
            "text": "A pesar de ti, de mi y del mundo que se desquebraja, yo te amo",
            "author": "Margareth Mitchell (Lo que el Viento se Llevó)"
        },
        {
            "text": "La alegría causa a veces un efecto extraño; oprime al corazón casi tanto como el dolor",
            "author": "Alejandro Dumas (El Conde de Montecristo)"
        },
        {
            "text": "Caminando en línea recta no puede uno llegar muy lejos",
            "author": "Antoine de Saint-Exupèry (El Principito)"
        },
        {
            "text": "Que cosa tan traicionera pensar que una persona es más que una persona",
            "author": "John Green (Paper Towns)"
        },
        {
            "text": "Se debe pedir a cada cual, lo que está a su alcance realizar",
            "author": "Antoine de Saint-Exupèry (El Principito)"
        },
        {
            "text": "Cuando una mujer se vuelve a casar es porque detestaba a su primer marido. Cuando un hombre se vuelve a casar es porque adoraba a su primera mujer. Las mujeres prueban suerte; los hombres arriesgan la suya",
            "author": "Oscar Wilde (El Retrato de Dorian Gray)"
        },
        {
            "text": "La muerte destroza al hombre: la idea de la muerte le salva",
            "author": "E. M. Forster (Howards End)"
        },
        {
            "text": "Cierto que casi siempre se encuentra algo, si se mira, pero no siempre es lo que uno busca",
            "author": "J.R.R. Tolkien (El Hobbit)"
        },
        {
            "text": "La dicha suprema de la vida es la convicción de que somos amados, amados por nosotros mismos; mejor dicho amados a pesar de nosotros",
            "author": "Victor Hugo (Los miserables)"
        },
        {
            "text": "Ningún hombre puede pensar claramente cuando sus puños están cerrados",
            "author": "George Jean Nathan"
        },
        {
            "text": "Un hombre que es un maestro en la paciencia es un maestro en todo lo demás",
            "author": "George Savile"
        },
        {
            "text": "Alguien que no cree en los milagros no es realista",
            "author": "David Ben-Gurión"
        },
        {
            "text": "No hay una visión más triste que la de un joven pesimista",
            "author": "Mark Twain"
        },
        {
            "text": "La esperanza es un buen desayuno, pero una mala cena",
            "author": "Francis Bacon"
        },
        {
            "text": "La educación es el movimiento de la oscuridad a la luz",
            "author": "Allan Bloom"
        },
        {
            "text": "El riesgo de una mala decisión es preferible al terror de la indecisión",
            "author": "Maimónides"
        },
        {
            "text": "Una mente necesita un libro como una espada necesita su piedra de afilar",
            "author": "George R. R. Martin"
        },
        {
            "text": "Lo que hoy está comprobado una vez solo pudo ser imaginado",
            "author": "William Blake"
        },
        {
            "text": "Solo los educados son libres",
            "author": "Epicteto"
        },
        {
            "text": "Todo conocimiento resulta hiriente",
            "author": "Cassandra Clare"
        },
        {
            "text": "La honestidad es el primer capítulo del libro de la sabiduría",
            "author": "Thomas Jefferson"
        },
        {
            "text": "Toda sociedad está a tres comidas del caos",
            "author": "Lenin"
        },
        {
            "text": "No se dice rompí a comer o rompí a caminar. Rompes a llorar o a reír. Creo que vale la pena hacerse añicos por esos sentimientos",
            "author": "Albert Espinosa"
        },
        {
            "text": "El tiempo es aquello que más queremos y también lo que peor utilizamos",
            "author": "William Penn"
        },
        {
            "text": "La libertad nunca es dada; siempre es ganada",
            "author": "Asa Philip Randolph"
        },
        {
            "text": "Una vez tienes algo que hacer, es mejor hacerlo que vivir con el miedo a causa de eso",
            "author": "Joe Abercrombie"
        },
        {
            "text": "El hombre es la única criatura que se niega a ser quien es",
            "author": "Albert Camus"
        },
        {
            "text": "La creatividad requiere que la valentía se desprenda de las certezas",
            "author": "Erich Fromm"
        },
        {
            "text": "La mejor parte de la belleza es aquella que ninguna imagen puede expresar",
            "author": "Francis Bacon"
        },
        {
            "text": "Aquellos que no conocen la historia están condenados a repetirla",
            "author": "Edmund Burke"
        },
        {
            "text": "Nada es tan increíble como para que la oratoria no lo pueda transformar en aceptable",
            "author": "Cicerón"
        },
        {
            "text": "De una pequeña chispa puede prender una llama",
            "author": "Dante"
        },
        {
            "text": "Con la Iglesia hemos dado, Sancho",
            "author": "Miguel de Cervantes (Don Quijote de la Mancha)"
        },
        {
            "text": "No hay libro tan malo que no tenga algo bueno",
            "author": "Miguel de Cervantes (Don Quijote de la Mancha)"
        },
        {
            "text": "Ser o no ser, esa es la cuestión",
            "author": "William Shakespeare (Hamlet)"
        },
        {
            "text": "Mire vuestra merced —respondió Sancho— que aquellos que allí se parecen no son gigantes, sino molinos de viento, y lo que en ellos parecen brazos son las aspas, que, volteadas del viento, hacen andar la piedra del molino",
            "author": "Miguel de Cervantes (Don Quijote de la Mancha)"
        },
        {
            "text": "Llegarás primero a las sirenas, que encantan a cuantos hombres van a su encuentro. Aquel que imprudentemente se acerca a ellas y oye su voz, ya no vuelve a ver a su esposa ni a sus hijos rodeándole, llenos de júbilo, cuando torna a su hogar",
            "author": "Homero (Odisea)"
        },
        {
            "text": "El presidio hace al presidiario",
            "author": "Victor Hugo (Los miserables)"
        },
        {
            "text": "Poderoso caballero es don Dinero",
            "author": "Francisco de Quevedo"
        },
        {
            "text": "Érase un hombre a una nariz pegado",
            "author": "Francisco de Quevedo (‘Soneto a una nariz’)"
        },
        {
            "text": "Ande yo caliente, / y ríase la gente",
            "author": "Luis de Góngora"
        },
        {
            "text": "Porque conformes a una, / con un valeroso pecho, / responden: Fuente Ovejuna",
            "author": "Lope de Vega (Fuenteovejuna)"
        },
        {
            "text": "¡Ah! ¿No es cierto, ángel de amor, / que en esta apartada orilla / más pura la luna brilla / y se respira mejor?",
            "author": "José Zorrilla (Don Juan Tenorio)"
        },
        {
            "text": "¿Qué es poesía?, dices mientras clavas / en mi pupila tu pupila azul. / ¿Qué es poesía? ¿Y tú me lo preguntas? / Poesía… eres tú",
            "author": "Gustavo Adolfo Bécquer (‘Rima XXI’)"
        },
        {
            "text": "Recuerde el alma dormida, / avive el seso y despierte / contemplando / cómo se pasa la vida, / cómo se viene la muerte / tan callando",
            "author": "Jorge Manrique (Coplas a la muerte de su padre)"
        },
        {
            "text": "Nuestras vidas son los ríos / que van a dar en la mar / que es el morir; / allí van los señoríos / derechos a se acabar / y consumir",
            "author": "Jorge Manrique (Coplas a la muerte de su padre)"
        },
        {
            "text": "Hombres necios que acusáis / a la mujer sin razón, / sin ver que sois la ocasión / de lo mismo que culpáis",
            "author": "Sor Juana Inés de la Cruz"
        },
        {
            "text": "Aunque la noche fue hecha para amar, / y demasiado pronto vuelven los días, / aún así no volveremos a vagar / a la luz de la luna",
            "author": "Lord Byron (‘No volveremos a vagar’)"
        },
        {
            "text": "Vivo sin vivir en mí / y tan alta vida espero, / que muero porque no muero",
            "author": "Santa Teresa de Jesús"
        },
        {
            "text": "Con diez cañones por banda, / viento en popa a toda vela, / no corta el mar, sino vuela / un velero bergantín",
            "author": "José de Espronceda (‘Canción del pirata’)"
        },
        {
            "text": "Pienso mesa y digo silla, / compro pan y me lo dejo, / lo que aprendo se me olvida, / lo que pasa es que te quiero",
            "author": "Gloria Fuertes"
        },
        {
            "text": "Se equivocó la paloma. / Se equivocaba",
            "author": "Rafael Alberti"
        },
        {
            "text": "Verde que te quiero verde / verde viento verdes ramas",
            "author": "Federico García Lorca"
        },
        {
            "text": "Mi infancia son recuerdos de un patio de Sevilla",
            "author": "Antonio Machado"
        },
        {
            "text": "Andaluces de Jaén, / aceituneros altivos, / decidme en el alma, ¿quién, / quién levantó los olivos?",
            "author": "Miguel Hernández (‘Aceituneros’)"
        },
        {
            "text": "…Y yo me iré. Y se quedarán los pájaros / cantando; / y se quedará mi huerto, con su verde árbol, / y con su pozo blanco",
            "author": "Juan Ramón Jiménez"
        },
        {
            "text": "Caminante no hay camino, se hace camino al andar",
            "author": "Antonio Machado"
        },
        {
            "text": "Mi amor y mis deseos no han variado; pero una palabra suya me hará callar para siempre",
            "author": "Jane Austen (Orgullo y prejuicio)"
        },
        {
            "text": "La palabra humana es como un caldero cascado en el que tocamos melodías para hacer bailar a los osos, cuando quisiéramos conmover a las estrellas",
            "author": "Gustave Flaubert (Madame Bovary)"
        },
        {
            "text": "No soy un pájaro y ninguna red me atrapa. Soy un ser humano libre con una voluntad independiente",
            "author": "Charlotte Brontë (Jane Eyre)"
        },
        {
            "text": "Andábamos sin buscarnos pero sabiendo que andábamos para encontrarnos",
            "author": "Julio Cortázar (Rayuela)"
        },
        {
            "text": "Solo con el corazón se puede ver bien; lo esencial es invisible a los ojos",
            "author": "Antoine de Saint-Exupéry (El principito)"
        },
        {
            "text": "¡Qué extraña cosa el conocimiento! Una vez que ha penetrado en la mente, se aferra a ella como la hiedra en la roca",
            "author": "Mary Shelley (Frankenstein)"
        },
        {
            "text": "No todo el oro reluce ni todos los errantes se han perdido",
            "author": "J. R. R. Tolkien (El Señor de los Anillos)"
        },
        {
            "text": "Creo que sí, estás loco. Pero te diré un secreto: las mejores personas lo están",
            "author": "Lewis Carroll (Alicia en el País de las Maravillas)"
        },
        {
            "text": "Nosotros, los habitantes de la Tierra, tenemos un talento especial para arruinar las cosas grandes y hermosas",
            "author": "Ray Bradbury (Crónicas marcianas)"
        },
        {
            "text": "Nada da un poder mayor sobre los hombres que las mentiras",
            "author": "Michael Ende (La historia interminable)"
        },
        {
            "text": "Preferiría no hacerlo",
            "author": "Herman Melville (Bartleby, el escribiente)"
        },
        {
            "text": "El hombre no está hecho para la derrota. Un hombre puede ser destruido, pero no derrotado",
            "author": "Ernest Hemingway (El viejo y el mar)"
        },
        {
            "text": "¡Alohomora!",
            "author": "J. K. Rowling (Harry Potter)"
        },
        {
            "text": "Me pregunté dónde se meterían los patos cuando venía el frío y se helaba la superficie del agua, si vendría un hombre a recogerlos en un camión para llevarlos al zoológico, o si se irían ellos a algún sitio por su cuenta",
            "author": "J. D. Salinger"
        },
        {
            "text": "Del mundo mundial",
            "author": "Elvira Lindo (Manolito Gafotas)"
        },
        {
            "text": "Era el mejor de los tiempos y el peor; la edad de la sabiduría y la de la tontería; la época de la fe y la época de la incredulidad; la estación de la Luz y de las Tinieblas; era la primavera de la esperanza y el invierno de la desesperación: todo se nos ofrecía como nuestro y no teníamos absolutamente nada; íbamos todos derechos al Cielo, todos nos precipitábamos en el infierno",
            "author": "Charles Dickens (Historia de dos ciudades)"
        },
        {
            "text": "No me atraparán",
            "author": "Francesco Pecoraro (La vida en tiempos de paz)"
        },
        {
            "text": "Nuestras vidas se definen por las oportunidades, incluso las que perdemos",
            "author": "F. Scott Fitzgerald (El curioso caso de Benjamin Button)"
        },
        {
            "text": "Cuando despertó, el dinosaurio todavía estaba allí",
            "author": "Augusto Monterroso (El dinosaurio)"
        },
        {
            "text": "En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor",
            "author": "Miguel de Cervantes (Don Quijote de la Mancha)"
        },
        {
            "text": "Al despertar Gregorio Samsa una mañana, tras un sueño intranquilo, encontróse en su cama convertido en un monstruoso insecto",
            "author": "Franz Kafka (La metamorfosis)"
        },
        {
            "text": "Al día siguiente no murió nadie",
            "author": "José Saramago (Las intermitencias de la muerte)"
        },
        {
            "text": "Muchos años después, frente al pelotón de fusilamiento, el coronel Aureliano Buendía había de recordar aquella tarde remota en que su padre lo llevó a conocer el hielo",
            "author": "Gabriel García Márquez (Cien años de soledad)"
        },
        {
            "text": "A pesar de que la mía es historia, no la empezaré por el arca de Noe y la genealogía de sus ascendientes como acostumbraban hacerlo los antiguos historiadores españoles de América que deben ser nuestro prototipos",
            "author": "Esteban Echeverría (El matadero)"
        },
        {
            "text": "La heroica ciudad dormía la siesta.",
            "author": "Leopoldo Alas “Clarín” (La Regenta)"
        }
    ],
    "en": [
        {
            "text": "To be or not to be, that is the question.",
            "author": "William Shakespeare"
        },
        {
            "text": "It was the best of times, it was the worst of times.",
            "author": "Charles Dickens"
        },
        {
            "text": "The only way to do great work is to love what you do.",
            "author": "Steve Jobs"
        },
        {
            "text": "Life is what happens when you're busy making other plans.",
            "author": "John Lennon"
        },
        {
            "text": "Success is not final, failure is not fatal: it is the courage to continue that counts.",
            "author": "Winston Churchill"
        }
    ]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/quote/<lang>')
def get_quote(lang):
    import random
    
    # Si el idioma no existe, usar inglés por defecto
    if lang not in QUOTES:
        lang = "en"
    
    # Seleccionar una cita aleatoria
    quote = random.choice(QUOTES[lang])
    return jsonify(quote)

@app.route('/api/verify', methods=['POST'])
def verify_text():
    data = request.json
    typed_text = data.get('typed', '')
    original_text = data.get('original', '')
    
    # Verificar la precisión
    min_length = min(len(typed_text), len(original_text))
    correct_chars = sum(1 for i in range(min_length) if typed_text[i] == original_text[i])
    accuracy = (correct_chars / len(original_text)) * 100 if len(original_text) > 0 else 0
    
    return jsonify({
        'accuracy': accuracy,
        'isCorrect': typed_text == original_text
    })

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)