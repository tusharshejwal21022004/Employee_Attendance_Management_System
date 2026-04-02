export function getPaginatedData(data: any[], page: number, pageSize: number) {
  return data.slice(0, pageSize);
}
