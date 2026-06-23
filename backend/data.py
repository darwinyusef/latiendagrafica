"""
Datos hardcodeados del sitio.
- imagen: URL string si hay foto; None si no hay → se usa icono/svg
- Para actualizar una imagen en runtime usa PUT /api/<tipo>/<id>/imagen
"""

SERVICIOS = [
    {
        "id": "gran-formato",
        "titulo": "Gran Formato",
        "descripcion": "Vallas, lonas y pendones de gran tamaño con impresión UV de alta resolución para exteriores e interiores.",
        "icono": None,
        "imagen": None,
        "svg": '<rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8M12 17v4"/><path d="M6 8h.01M6 11h8"/>',
        "color_fondo": "#EFF6FF",
        "color_trazo": "#1E40AF",
    },
    {
        "id": "digital",
        "titulo": "Digital",
        "descripcion": "Tarjetas, volantes, flyers y material POP con impresión digital offset de precisión y colores vibrantes.",
        "icono": None,
        "imagen": None,
        "svg": '<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/>',
        "color_fondo": "#F0FDF4",
        "color_trazo": "#16A34A",
    },
    {
        "id": "dtf",
        "titulo": "DTF",
        "descripcion": "Estampado directo al tejido en alta definición. Ideal para camisetas, busos y prendas de cualquier color.",
        "icono": None,
        "imagen": None,
        "svg": '<path d="M20.38 3.46L16 2a4 4 0 01-8 0L3.62 3.46a2 2 0 00-1.34 2.23l.58 3.57a1 1 0 00.99.84H7v10c0 1.1.9 2 2 2h6a2 2 0 002-2V10h3.15a1 1 0 00.99-.84l.58-3.57a2 2 0 00-1.34-2.23z"/>',
        "color_fondo": "#FFF7ED",
        "color_trazo": "#EA580C",
    },
    {
        "id": "sublimacion",
        "titulo": "Sublimación",
        "descripcion": "Personalización total en tazas, gorras, cojines y artículos promocionales con colores que no se desvanecen.",
        "icono": None,
        "imagen": None,
        "svg": '<path d="M17 8h1a4 4 0 010 8h-1"/><path d="M3 8h14v9a4 4 0 01-4 4H7a4 4 0 01-4-4V8z"/><line x1="6" y1="2" x2="6" y2="4"/><line x1="10" y1="2" x2="10" y2="4"/><line x1="14" y1="2" x2="14" y2="4"/>',
        "color_fondo": "#FDF4FF",
        "color_trazo": "#9333EA",
    },
]

CATALOGO = [
    # ── ADHESIVOS ──
    {"id": "stickers-personalizados",  "nombre": "Stickers Personalizados",   "precio": "Desde $30.000 COP", "descripcion": "Vinilo de alta calidad, resistente al agua y al sol.",       "categoria": "adhesivos", "icono": "🏷️", "imagen": None, "gradiente": "#FEF9C3,#FDE047"},
    {"id": "vinilos-decorativos",       "nombre": "Vinilos Decorativos",        "precio": "Desde $25.000 COP", "descripcion": "Para vidrieras, paredes y cualquier superficie lisa.",       "categoria": "adhesivos", "icono": "🔖",  "imagen": None, "gradiente": "#FEF3C7,#FDE68A"},
    {"id": "vinilo-de-corte",           "nombre": "Vinilo de Corte",            "precio": "Desde $35.000 COP", "descripcion": "Lettering y formas de precisión en vinilo de plóter.",      "categoria": "adhesivos", "icono": "✂️",  "imagen": None, "gradiente": "#FFF7ED,#FED7AA"},
    {"id": "etiquetas-adhesivas",       "nombre": "Etiquetas Adhesivas",        "precio": "Desde $22.000 COP", "descripcion": "Etiquetas personalizadas para productos y empaques.",        "categoria": "adhesivos", "icono": "🏷️", "imagen": None, "gradiente": "#FFFBEB,#FEF08A"},
    {"id": "letras-de-corte",           "nombre": "Letras de Corte",            "precio": "Desde $40.000 COP", "descripcion": "Letras en vinilo para fachadas, tiendas y locales.",        "categoria": "adhesivos", "icono": "🔤",  "imagen": None, "gradiente": "#FFF7ED,#FDBA74"},
    # ── TARJETAS ──
    {"id": "tarjetas-de-presentacion",  "nombre": "Tarjetas de Presentación",   "precio": "Desde $45.000 COP", "descripcion": "Couché premium, acabado mate o brillo a elección.",         "categoria": "tarjetas",  "icono": "💳",  "imagen": None, "gradiente": "#DBEAFE,#93C5FD"},
    {"id": "volantes-y-flyers",         "nombre": "Volantes y Flyers",          "precio": "Desde $35.000 COP", "descripcion": "Carta, media carta o formato completamente personalizado.", "categoria": "tarjetas",  "icono": "📄",  "imagen": None, "gradiente": "#E0F2FE,#7DD3FC"},
    {"id": "postales",                  "nombre": "Postales",                   "precio": "Desde $38.000 COP", "descripcion": "Acabados especiales y alta definición en cada pieza.",      "categoria": "tarjetas",  "icono": "📮",  "imagen": None, "gradiente": "#EFF6FF,#BFDBFE"},
    {"id": "folletos-plegables",        "nombre": "Folletos Plegables",         "precio": "Desde $55.000 COP", "descripcion": "Díptico, tríptico o Z-fold en papel couché.",              "categoria": "tarjetas",  "icono": "📋",  "imagen": None, "gradiente": "#DBEAFE,#60A5FA"},
    {"id": "carpetas-impresas",         "nombre": "Carpetas Impresas",          "precio": "Desde $75.000 COP", "descripcion": "Carpetas corporativas con impresión full color.",           "categoria": "tarjetas",  "icono": "📁",  "imagen": None, "gradiente": "#EFF6FF,#93C5FD"},
    # ── BANNERS ──
    {"id": "banners-publicitarios",     "nombre": "Banners Publicitarios",      "precio": "Desde $120.000 COP","descripcion": "Lona de alta resistencia para uso en exteriores.",         "categoria": "banners",   "icono": "🏳️", "imagen": None, "gradiente": "#D1FAE5,#6EE7B7"},
    {"id": "pendones-roll-up",          "nombre": "Pendones Roll-up",           "precio": "Desde $160.000 COP","descripcion": "Estructura metálica incluida, montaje en segundos.",       "categoria": "banners",   "icono": "🎌",  "imagen": None, "gradiente": "#DCFCE7,#86EFAC"},
    {"id": "vallas-exteriores",         "nombre": "Vallas Exteriores",          "precio": "Desde $250.000 COP","descripcion": "Gran impacto visual, totalmente resistente al clima.",     "categoria": "banners",   "icono": "🪧",  "imagen": None, "gradiente": "#F0FDF4,#BBF7D0"},
    {"id": "lonas-de-eventos",          "nombre": "Lonas de Eventos",           "precio": "Desde $180.000 COP","descripcion": "Ideal para ferias, activaciones y eventos corporativos.", "categoria": "banners",   "icono": "🎪",  "imagen": None, "gradiente": "#ECFDF5,#A7F3D0"},
    {"id": "back-lights",               "nombre": "Back-lights",                "precio": "Desde $300.000 COP","descripcion": "Impresión translúcida para cajas de luz y retroiluminados.","categoria": "banners", "icono": "💡",  "imagen": None, "gradiente": "#D1FAE5,#4ADE80"},
    # ── TEXTIL ──
    {"id": "camisetas-estampadas",      "nombre": "Camisetas Estampadas",       "precio": "Desde $50.000 COP", "descripcion": "Estampado DTF de larga duración, 100% algodón suave.",     "categoria": "textil",    "icono": "👕",  "imagen": None, "gradiente": "#FCE7F3,#F9A8D4"},
    {"id": "gorras-personalizadas",     "nombre": "Gorras Personalizadas",      "precio": "Desde $40.000 COP", "descripcion": "Bordado o estampado DTF en varios colores y estilos.",     "categoria": "textil",    "icono": "🧢",  "imagen": None, "gradiente": "#FDF2F8,#F0ABFC"},
    {"id": "hoodies-y-chaquetas",       "nombre": "Hoodies y Chaquetas",        "precio": "Desde $85.000 COP", "descripcion": "Estampado premium, lavable a máquina sin decoloración.",  "categoria": "textil",    "icono": "🧥",  "imagen": None, "gradiente": "#FFF1F2,#FDA4AF"},
    {"id": "bolsas-de-tela",            "nombre": "Bolsas de Tela",             "precio": "Desde $30.000 COP", "descripcion": "Bolsas reutilizables con diseño full color.",              "categoria": "textil",    "icono": "👜",  "imagen": None, "gradiente": "#FCE7F3,#FBCFE8"},
    {"id": "camisetas-polo",            "nombre": "Camisetas Polo",             "precio": "Desde $65.000 COP", "descripcion": "Estampado o bordado en pecho y manga, varios colores.",   "categoria": "textil",    "icono": "👔",  "imagen": None, "gradiente": "#FDF4FF,#F5D0FE"},
    {"id": "delantales-personalizados", "nombre": "Delantales Personalizados",  "precio": "Desde $45.000 COP", "descripcion": "Ideal para restaurantes, talleres y eventos gastronómicos.","categoria": "textil", "icono": "🧑‍🍳","imagen": None, "gradiente": "#FFF1F2,#FECDD3"},
    # ── OTROS ──
    {"id": "tazas-sublimadas",          "nombre": "Tazas Sublimadas",           "precio": "Desde $28.000 COP", "descripcion": "Personalización total en 360°, perfectas para regalo.",    "categoria": "otros",     "icono": "☕",  "imagen": None, "gradiente": "#EDE9FE,#C4B5FD"},
    {"id": "llaveros-dtf-uv",           "nombre": "Llaveros DTF UV",            "precio": "Desde $15.000 COP", "descripcion": "Acrílico o MDF con diseño full color de alta definición.", "categoria": "otros",     "icono": "🔑",  "imagen": None, "gradiente": "#F5F3FF,#DDD6FE"},
    {"id": "almohadas-sublimadas",      "nombre": "Almohadas Sublimadas",       "precio": "Desde $45.000 COP", "descripcion": "Diseño personalizado con colores vivos y duraderos.",      "categoria": "otros",     "icono": "🛋️", "imagen": None, "gradiente": "#FAF5FF,#E9D5FF"},
    {"id": "lapiceros-personalizados",  "nombre": "Lapiceros Personalizados",   "precio": "Desde $12.000 COP", "descripcion": "Impresión del logo corporativo con acabado profesional.",  "categoria": "otros",     "icono": "🖊️", "imagen": None, "gradiente": "#F3E8FF,#D8B4FE"},
    {"id": "porta-retratos-sublimados", "nombre": "Porta-retratos Sublimados",  "precio": "Desde $35.000 COP", "descripcion": "Marco de MDF con foto impresa de alta resolución.",        "categoria": "otros",     "icono": "🖼️", "imagen": None, "gradiente": "#EDE9FE,#A78BFA"},
    {"id": "mousepads-personalizados",  "nombre": "Mousepads Personalizados",   "precio": "Desde $28.000 COP", "descripcion": "Base antideslizante con impresión full color y brillo.",   "categoria": "otros",     "icono": "🖥️", "imagen": None, "gradiente": "#F5F3FF,#C4B5FD"},
]

PORTAFOLIO = [
    # ── GRAN FORMATO ──
    {"id": "valla-corporativa-logistica",    "titulo": "Valla Corporativa Empresa Logística",      "cliente": "Cliente: Sector Transporte",     "descripcion": "Valla de 6×3 m en lona blackout con impresión UV de alta resolución para fachada exterior.",                                           "categoria": "gran-formato",  "icono": "🪧",  "imagen": "https://media.staticontent.com/media/pictures/dc67e06e-64f5-4c9e-8a36-b95e127f7bb3/1100x900", "gradiente": "#D1FAE5,#34D399", "etiquetas": ["Lona", "6×3 m", "Exterior"]},
    {"id": "pendon-rollup-feria",            "titulo": "Pendón Roll-up Feria Empresarial",         "cliente": "Cliente: Sector Salud",          "descripcion": "Pendón de 85×200 cm con estructura metálica incluida, diseño corporativo con degradados.",                                             "categoria": "gran-formato",  "icono": "🎌",  "imagen": None, "gradiente": "#DCFCE7,#86EFAC", "etiquetas": ["Roll-up", "85×200 cm", "Indoor"]},
    {"id": "backlight-centro-comercial",     "titulo": "Back-light Centro Comercial",              "cliente": "Cliente: Retail",                "descripcion": "Impresión translúcida en material back-light para caja de luz de 2×1 m, colores vibrantes 24/7.",                                    "categoria": "gran-formato",  "icono": "💡",  "imagen": None, "gradiente": "#ECFDF5,#A7F3D0", "etiquetas": ["Back-light", "2×1 m", "Retroiluminado"]},
    {"id": "lonas-activacion-marca",         "titulo": "Lonas Evento Activación de Marca",         "cliente": "Cliente: Bebidas",               "descripcion": "Set de 4 lonas temáticas de 3×2 m para activación BTL en punto de venta y eventos outdoor.",                                          "categoria": "gran-formato",  "icono": "🎪",  "imagen": None, "gradiente": "#F0FDF4,#BBF7D0", "etiquetas": ["Lona", "BTL", "Set ×4"]},
    # ── DIGITAL ──
    {"id": "tarjetas-presentacion-premium",  "titulo": "Tarjetas de Presentación Premium",         "cliente": "Cliente: Consultoría Jurídica",  "descripcion": "1.000 tarjetas en couché 350 g con barniz UV selectivo y diseño minimalista en dos tintas.",                                          "categoria": "digital",       "icono": "💳",  "imagen": None, "gradiente": "#DBEAFE,#93C5FD", "etiquetas": ["Couché 350g", "UV Selectivo", "1.000 uds"]},
    {"id": "flyers-campana-lanzamiento",     "titulo": "Flyers Campaña Lanzamiento",               "cliente": "Cliente: Restaurante",           "descripcion": "5.000 flyers tamaño media carta en couché brillante 150 g con diseño a full color para reparto.",                                     "categoria": "digital",       "icono": "📄",  "imagen": None, "gradiente": "#E0F2FE,#7DD3FC", "etiquetas": ["Media carta", "Brillante", "5.000 uds"]},
    {"id": "folleto-triptico-corporativo",   "titulo": "Folleto Tríptico Corporativo",             "cliente": "Cliente: Constructora",          "descripcion": "Folleto tríptico A4 en couché mate 200 g con paleta cromática corporativa y fotografía de alta calidad.",                              "categoria": "digital",       "icono": "📋",  "imagen": None, "gradiente": "#EFF6FF,#BFDBFE", "etiquetas": ["Tríptico", "A4", "Couché mate"]},
    {"id": "carpetas-corporativas",          "titulo": "Carpetas Corporativas",                    "cliente": "Cliente: Firma Contable",        "descripcion": "200 carpetas media carta con bolsillo interior, logo en relieve y tiro/retiro full color.",                                            "categoria": "digital",       "icono": "📁",  "imagen": None, "gradiente": "#DBEAFE,#60A5FA", "etiquetas": ["Media carta", "Relieve", "200 uds"]},
    # ── DTF ──
    {"id": "uniformes-club-futbol",          "titulo": "Uniformes Deportivos Club Fútbol",         "cliente": "Cliente: Club Deportivo",        "descripcion": "30 camisetas con escudo, nombre y número en DTF full color. Alta durabilidad al lavado.",                                              "categoria": "dtf",           "icono": "⚽",  "imagen": None, "gradiente": "#FCE7F3,#F9A8D4", "etiquetas": ["Camisetas", "30 uds", "Full color"]},
    {"id": "camisetas-evento-corporativo",   "titulo": "Camisetas Evento Corporativo",             "cliente": "Cliente: Empresa Tech",          "descripcion": "80 camisetas polo con logo institucional estampado en DTF para jornada de integración empresarial.",                                  "categoria": "dtf",           "icono": "👕",  "imagen": None, "gradiente": "#FDF2F8,#F0ABFC", "etiquetas": ["Polo", "80 uds", "Institucional"]},
    {"id": "gorras-linea-premium",           "titulo": "Gorras Personalizadas Línea Premium",      "cliente": "Cliente: Marca Urbana",          "descripcion": "50 gorras dad hat en 5 colores con parche frontal DTF de alta definición y ala plana.",                                               "categoria": "dtf",           "icono": "🧢",  "imagen": None, "gradiente": "#FFF1F2,#FDA4AF", "etiquetas": ["Gorras", "50 uds", "5 colores"]},
    {"id": "tote-bag-feria",                 "titulo": "Bolsas Tote Bag Feria",                    "cliente": "Cliente: Editorial",             "descripcion": "200 bolsas de tela en algodón natural con diseño ilustrado estampado en DTF para evento literario.",                                  "categoria": "dtf",           "icono": "👜",  "imagen": None, "gradiente": "#FCE7F3,#FBCFE8", "etiquetas": ["Tote bag", "200 uds", "Algodón"]},
    # ── SUBLIMACIÓN ──
    {"id": "tazas-coleccion-navidena",       "titulo": "Tazas Colección Navideña",                 "cliente": "Cliente: Empresa Alimentos",     "descripcion": "120 tazas sublimadas con diseño navideño personalizado para kit de regalo corporativo.",                                            "categoria": "sublimacion",   "icono": "☕",  "imagen": None, "gradiente": "#EDE9FE,#C4B5FD", "etiquetas": ["Tazas", "120 uds", "Kit regalo"]},
    {"id": "almohadas-decorativas",          "titulo": "Almohadas Decorativas Personalizadas",     "cliente": "Cliente: Tienda Online",         "descripcion": "60 almohadas de 40×40 cm con diseño full color sublimado, relleno incluido y acabado premium.",                                      "categoria": "sublimacion",   "icono": "🛋️", "imagen": None, "gradiente": "#FAF5FF,#E9D5FF", "etiquetas": ["40×40 cm", "60 uds", "Relleno incl."]},
    {"id": "porta-retratos-mdf",             "titulo": "Porta-retratos Marco MDF",                 "cliente": "Cliente: Fotografía",            "descripcion": "40 porta-retratos en MDF 15×20 cm con imagen sublimada de alta resolución para galería de exposición.",                               "categoria": "sublimacion",   "icono": "🖼️", "imagen": None, "gradiente": "#F5F3FF,#DDD6FE", "etiquetas": ["MDF", "15×20 cm", "40 uds"]},
    {"id": "mousepad-corporativo",           "titulo": "Mousepad Corporativo",                     "cliente": "Cliente: Agencia Digital",       "descripcion": "100 mousepads con logo y paleta corporativa en sublimación full color, base antideslizante.",                                         "categoria": "sublimacion",   "icono": "🖥️", "imagen": None, "gradiente": "#F3E8FF,#D8B4FE", "etiquetas": ["Mousepad", "100 uds", "Antideslizante"]},
]
