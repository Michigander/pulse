import {html, svg} from 'https://unpkg.com/lit-html?module';

const citizen = ({isActive}) => svg`
  <svg viewBox="0 0 100 100" height="24" width="24">
    <circle cx="50" cy="50" r="50" fill=${isActive ? "salmon" : "black"} />
  </svg>
`

export default (state) => state.users.map((id) => citizen({
  isActive: id === state.id
}))
