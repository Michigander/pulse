import {render} from 'https://unpkg.com/lit-html?module';

export default (conduit, client) => {
  return conduit((data) => render(client(data), document.body))
}
