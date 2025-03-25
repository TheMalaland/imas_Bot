const generateAuthLink = () => {
    const clientKey = process.env.CLIENT_KEY;
    const redirectUri = process.env.REDIRECT_URI;
    const scope = 'user.info.basic,video.upload'; // Puedes añadir más scopes si necesitas
  
    const authLink = `https://open-api.tiktok.com/platform/oauth/connect?client_key=${clientKey}&scope=${scope}&response_type=code&redirect_uri=${encodeURIComponent(redirectUri)}&state=random_string`;
  
    console.log('Visita el siguiente enlace en tu navegador para autorizar la aplicación:');
    console.log(authLink);
  };
  