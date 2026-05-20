import { HttpInterceptorFn } from '@angular/common/http';
import { catchError, throwError } from 'rxjs';

export const httpErrorInterceptor: HttpInterceptorFn = (req, next) => {
  return next(req).pipe(
    catchError((error) => {
      if (error.status === 0) {
        console.error('[HTTP] Network error — verifica que el backend esté activo en :8000');
      } else {
        console.error(`[HTTP] Error ${error.status}: ${error.message}`);
      }
      return throwError(() => error);
    }),
  );
};
