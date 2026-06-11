import { BookOpen, Home } from 'lucide-react';
import { useRouter } from 'next/router';

import { Head } from '@/components/seo';
import { Button } from '@/components/ui/button';
import { paths } from '@/config/paths';
import { useUser } from '@/lib/auth';

export const HomePage = () => {
  const router = useRouter();
  const user = useUser();

  const handleStart = () => {
    if (user.data) {
      router.push(paths.app.dashboard.getHref());
    } else {
      router.push(paths.auth.login.getHref());
    }
  };

  return (
    <>
      <Head
        title={'Next.js Pages Router Toolkit'}
        description="Reusable Pages Router skeleton for API-backed product frontends"
      />
      <div className="flex h-screen items-center bg-white">
        <div className="mx-auto max-w-7xl px-4 py-12 text-center sm:px-6 lg:px-8 lg:py-16">
          <h2 className="text-3xl font-extrabold tracking-tight text-gray-900 sm:text-4xl">
            <span className="block">Next.js Pages Router Toolkit</span>
          </h2>
          <img src="/logo.svg" alt="react" />
          <p>Reusable Pages Router skeleton for API-backed product frontends</p>
          <div className="mt-8 flex justify-center">
            <div className="inline-flex rounded-md shadow">
              <Button onClick={handleStart} icon={<Home className="size-6" />}>
                Get started
              </Button>
            </div>
            <div className="ml-3 inline-flex">
              <a
                href="https://nextjs.org/docs/pages"
                target="_blank"
                rel="noreferrer"
              >
                <Button
                  variant="outline"
                  icon={<BookOpen className="size-6" />}
                >
                  Next.js Docs
                </Button>
              </a>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default HomePage;
