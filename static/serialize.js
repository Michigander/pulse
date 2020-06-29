export default (event) => {
  return JSON.stringify({
    type: event.type,
    meta: event.detail && event.detail.meta,
    payload: event.detail && event.detail.payload,
  })
}
