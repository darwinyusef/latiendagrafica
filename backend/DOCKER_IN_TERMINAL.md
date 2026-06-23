pción recomendada: Docker Engine en WSL2

  Paso 1 — Instalar WSL2 con una distro mínima

  # Instalar WSL2
  wsl --install --no-distribution

  # Instalar Ubuntu minimal (o Alpine si quieres aún menos peso)
  wsl --install -d Ubuntu

  Paso 2 — Instalar Docker Engine dentro de WSL2

  Dentro de la terminal WSL2 (Ubuntu):
  # Dependencias mínimas
  sudo apt-get update
  sudo apt-get install -y ca-certificates curl gnupg

  # Repositorio oficial de Docker
  sudo install -m 0755 -d /etc/apt/keyrings
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o 
  /etc/apt/keyrings/docker.gpg
  echo "deb [arch=$(dpkg --print-architecture)
  signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu  $(. /etc/os-release && echo $VERSION_CODENAME) stable" | sudo tee
  /etc/apt/sources.list.d/docker.list

  # Instalar solo el engine (sin Desktop)
  sudo apt-get update
  sudo apt-get install -y docker-ce docker-ce-cli containerd.io

  # Arrancar sin systemd (WSL no tiene systemd por defecto)
  sudo dockerd &

  Paso 3 — Iniciar Docker automáticamente al abrir WSL

  Agrega esto a tu ~/.bashrc o ~/.profile:
  if [ "$(ps -e | grep -c dockerd)" -lt 1 ]; then
    sudo dockerd > /dev/null 2>&1 &
  fi

  ---
  Mover WSL2 a H: o I: (para no consumir espacio en C:)

  wsl --shutdown
  wsl --export Ubuntu "H:\wsl-backup\ubuntu.tar"
  wsl --unregister Ubuntu
  wsl --import Ubuntu "H:\wsl\ubuntu" "H:\wsl-backup\ubuntu.tar" --version 2      

  ---
  Comparativa de peso

  ┌───────────────────────┬─────────────┬──────────────┐
  │       Solución        │ RAM aprox.  │ Disco aprox. │
  ├───────────────────────┼─────────────┼──────────────┤
  │ Docker Desktop        │ ~1-2 GB     │ ~4-6 GB      │
  ├───────────────────────┼─────────────┼──────────────┤
  │ Docker Engine en WSL2 │ ~200-400 MB │ ~1-2 GB      │
  └───────────────────────┴─────────────┴──────────────┘

  Sin GUI, sin servicios en segundo plano de Windows, solo el daemon cuando lo    
  necesitas. ¿Tienes WSL2 ya instalado?