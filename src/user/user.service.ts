import bcrypt from 'bcryptjs';

export async function saveUser(password: string) {
  const hash = await bcrypt.hash(password, 10);
  return hash;
}