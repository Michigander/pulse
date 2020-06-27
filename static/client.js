import {html} from 'https://unpkg.com/lit-html?module';

export default (state) => html`
  ${JSON.stringify(state)}
`
