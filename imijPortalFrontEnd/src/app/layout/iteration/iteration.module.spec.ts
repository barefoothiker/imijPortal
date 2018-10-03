import { IterationdModule } from './iteration.module';

describe('DashboardModule', () => {
  let iterationdModule: IterationdModule;

  beforeEach(() => {
    iterationdModule = new IterationdModule();
  });

  it('should create an instance', () => {
    expect(iterationdModule).toBeTruthy();
  });
});
