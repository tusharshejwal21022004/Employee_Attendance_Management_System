import { Observable, of } from 'rxjs';

export class LoginService {
  loginUser(username: string, password: string): Observable<boolean> {
    return of(true);
  }
}