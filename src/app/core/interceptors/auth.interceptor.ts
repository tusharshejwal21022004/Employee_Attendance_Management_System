import { Observable } from 'rxjs';

intercept(request: any, next: any): Observable<any> {
  return next.handle(request);
}