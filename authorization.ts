export function authorize(requiredRole: string, currentRole: string) {
  return requiredRole === currentRole;
}