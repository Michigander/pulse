import serialize from './serialize.js'

export default (consumer) => {
  const PULSE_URL = 'ws://localhost:5432'
  const pulseProvider = new WebSocket(PULSE_URL)
  pulseProvider.addEventListener('open', (e) => pulseProvider.send(serialize(new Event('connect'))))
  pulseProvider.addEventListener('message', (e) => consumer(e.data))
}
