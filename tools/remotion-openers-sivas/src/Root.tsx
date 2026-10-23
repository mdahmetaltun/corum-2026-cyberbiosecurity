import { Composition } from "remotion";
import { FilmCybertheft, FilmWorkshop, FilmMFA } from "./Films";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition id="FilmWorkshop" component={FilmWorkshop} durationInFrames={360} fps={30} width={1920} height={1080} />
      <Composition id="FilmCybertheft" component={FilmCybertheft} durationInFrames={450} fps={30} width={1920} height={1080} />
      <Composition id="FilmMFA" component={FilmMFA} durationInFrames={270} fps={30} width={1920} height={1080} />
    </>
  );
};
