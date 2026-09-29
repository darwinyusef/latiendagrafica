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
    {"id": "adhesivo-papel",            "nombre": "Adhesivo Papel",             "precio": "Precio a cotizar",  "descripcion": "La opción más tradicional y económica. Perfecto para personalizar agendas, empaques, bolsas de despacho o cajas de cartón.", "categoria": "adhesivos", "icono": "🏷️", "imagen": "images/catalogo/adhesivo-papel.jpg", "gradiente": "#FFF7ED,#FDBA74", "ficha": "images/fichas/adhesivo-comparativa.jpg"},
    {"id": "adhesivo-vinilo",           "nombre": "Adhesivo Vinilo",            "precio": "Precio a cotizar",  "descripcion": "Stickers y etiquetas que lo aguantan todo. El adhesivo vinilo está diseñado para resistir las condiciones más exigentes sin perder color ni romperse.", "categoria": "adhesivos", "icono": "🏷️", "imagen": "images/catalogo/adhesivo-vinilo.jpg", "gradiente": "#FFF7ED,#FDBA74", "ficha": "images/fichas/adhesivo-comparativa.jpg"},
    # ── TARJETAS ──
    {"id": "tarjetas-de-presentacion",  "nombre": "Tarjetas de Presentación",   "precio": "Precio a cotizar", "descripcion": "Nuestro paquete de 1.000 de tarjetas de presentación es la extensión de tu marca y tu profesionalismo en cada reunión, feria o evento comercial.",         "categoria": "tarjetas",  "icono": "💳",  "imagen": "/images/catalogo/tarjetaspresentacion.jpg", "gradiente": "#DBEAFE,#93C5FD", "ficha": "images/fichas/tarjetas-ficha.jpg"},
    {"id": "volantes-y-flyers",         "nombre": "Volantes y Flyers",          "precio": "Precio a cotizar", "descripcion": "Nuestro paquete de 1.000 volantes a full color es la herramienta perfecta para masificar tu mensaje, anunciar promociones, lanzar nuevos productos o hacer que todo el barrio conozca tu marca.", "categoria": "tarjetas",  "icono": "📄",  "imagen": "images/catalogo/volantes.jpg", "gradiente": "#E0F2FE,#7DD3FC"},
    {"id": "impresion-laser",           "nombre": "Impresión Láser",            "precio": "Precio a cotizar",  "descripcion": "La tecnología láser ofrece un tramado ultra fino que respeta los degradados, las luces y las sombras de tus imágenes. Colores vivos, negros profundos y durabilidad excepcional en papeles de alto gramaje.", "categoria": "tarjetas", "icono": "🖨️", "imagen": "images/catalogo/impresion-laser.jpg", "gradiente": "#DBEAFE,#93C5FD"},
    {"id": "agenda-personalizada",      "nombre": "Agenda Personalizada",       "precio": "Precio a cotizar",  "descripcion": "Agendas personalizadas con adhesivo papel, ideales para regalos corporativos y uso de oficina.", "categoria": "tarjetas", "icono": "📓", "imagen": "images/catalogo/agenda-personalizada.jpg", "gradiente": "#E0F2FE,#7DD3FC"},
    # ── BANNERS ──
    {"id": "impresion-gran-formato",    "nombre": "Impresión Gran Formato",     "precio": "Precio a cotizar",  "descripcion": "Transforma un espacio comercial o haz que la fachada de tu negocio hable por sí sola. La Impresión a Gran Formato es la herramienta publicitaria definitiva.", "categoria": "banners", "icono": "🏢", "imagen": "images/catalogo/gran-formato.jpg", "gradiente": "#D1FAE5,#6EE7B7", "ficha": "images/fichas/gran-formato-garantia.jpg"},
    {"id": "lona-publicitaria",         "nombre": "Lona Publicitaria",          "precio": "Precio a cotizar",  "descripcion": "Lonas y pendones (banners): el estándar de la publicidad exterior por su excelente relación costo-beneficio y máxima durabilidad.", "categoria": "banners", "icono": "🏳️", "imagen": "images/catalogo/lona-publicitaria.jpg", "gradiente": "#DCFCE7,#86EFAC"},
    # ── TEXTIL ──
    {"id": "estampado-dtf",             "nombre": "Estampado DTF",              "precio": "Precio a cotizar",  "descripcion": "Con el DTF obtienes imágenes a todo color, con una nitidez impresionante y una resistencia al lavado insuperable. Ideal para camisetas, chaquetas, gorras y bolsos.", "categoria": "textil", "icono": "👕", "imagen": "images/catalogo/dtf.jpg", "gradiente": "#FCE7F3,#F9A8D4"},
    # ── OTROS ──
    {"id": "mug-personalizado",         "nombre": "Mug Personalizado",          "precio": "Precio a cotizar",  "descripcion": "Un mug personalizado es la compañía perfecta para iniciar el día, trabajar en la oficina o sorprender con un regalo inolvidable. Alta definición y resistencia al microondas y al lavado diario.", "categoria": "otros", "icono": "☕", "imagen": "images/catalogo/mug.jpg", "gradiente": "#EDE9FE,#C4B5FD", "ficha": "images/fichas/mug-ficha.jpg"},
    {"id": "cuadros-mdf",               "nombre": "Cuadros en MDF",             "precio": "Precio a cotizar",  "descripcion": "Alternativa moderna, económica y elegante a los marcos tradicionales con vidrio. Estructura sólida y ligera con estilo minimalista, la imagen se extiende hasta el borde de la madera.", "categoria": "otros", "icono": "🖼️", "imagen": "images/catalogo/mdf.jpg", "gradiente": "#F5F3FF,#DDD6FE", "ficha": "images/fichas/mdf-garantia.jpg"},
    {"id": "impresion-3d",              "nombre": "Impresión 3D",               "precio": "Precio a cotizar",  "descripcion": "Imprimimos con tecnología de alta precisión para garantizar estructuras sólidas, acabados limpios y la máxima fidelidad a tu diseño original.", "categoria": "otros", "icono": "🧊", "imagen": "images/catalogo/impresion-3d.jpg", "gradiente": "#EDE9FE,#A78BFA"},
    {"id": "padmouse-sublimado",        "nombre": "Padmouse Sublimado",         "precio": "Precio a cotizar",  "descripcion": "Mouse pads con tecnología de sublimación textil de alta definición: un producto funcional, estético y de larga duración.", "categoria": "otros", "icono": "🖱️", "imagen": "images/catalogo/padmouse.jpg", "gradiente": "#F3E8FF,#D8B4FE", "ficha": "images/fichas/padmouse-ficha.jpg"},
    {"id": "pines-personalizados",      "nombre": "Pines Personalizados",       "precio": "Precio a cotizar",  "descripcion": "Herramienta publicitaria sutil, elegante y de alto impacto que transforma cualquier prenda, maleta o accesorio en un canal de comunicación para tu marca.", "categoria": "otros", "icono": "📌", "imagen": "images/catalogo/pines.jpg", "gradiente": "#F5F3FF,#E9D5FF", "ficha": "images/fichas/pines-ficha.jpg"},
]

SENALIZACION = [
    {"id": "letreros-publicitarios",    "nombre": "Letreros Publicitarios",     "precio": "Precio a cotizar",  "descripcion": "La fachada de tu negocio es tu mejor tarjeta de presentación. Letreros en poliacrílico, una imagen moderna, premium y profesional.", "categoria": "senalizacion", "icono": "🪧", "imagen": "images/catalogo/letrero.jpg", "gradiente": "#FEF3C7,#FCD34D", "ficha": "images/fichas/letrero-garantia.jpg"},
    {"id": "placas-reglamentarias",     "nombre": "Placas Reglamentarias",      "precio": "Precio a cotizar",  "descripcion": "Placas a la medida en acrílico o PVC de alta resistencia, con buenos acabados e impresión directa que garantizan máxima durabilidad ante el sol, el agua y el uso rudo.", "categoria": "senalizacion", "icono": "🚧", "imagen": "images/catalogo/placa-reglamentaria.jpg", "gradiente": "#FEF9C3,#FDE047"},
    {"id": "placas-de-reconocimiento",  "nombre": "Placas de Reconocimiento",   "precio": "Precio a cotizar",  "descripcion": "Gracias al corte láser de precisión logramos textos ultra nítidos, logotipos institucionales a todo color y detalles de alta fidelidad que no se borran con el tiempo.", "categoria": "senalizacion", "icono": "🏅", "imagen": "images/catalogo/placa-reconocimiento.jpg", "gradiente": "#FFEDD5,#FDBA74"},
]

CATALOGO = CATALOGO + SENALIZACION

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
